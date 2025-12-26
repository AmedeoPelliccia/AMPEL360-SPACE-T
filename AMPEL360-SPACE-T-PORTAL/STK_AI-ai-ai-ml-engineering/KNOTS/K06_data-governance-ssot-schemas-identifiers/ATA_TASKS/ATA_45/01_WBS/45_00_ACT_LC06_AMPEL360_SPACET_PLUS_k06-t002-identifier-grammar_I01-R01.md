## T002 — Identifier grammar (Must Have)

**Intent**
Define a **canonical identifier grammar** for:

* **Messages** (catalog entries, error codes, notifications)
* **Topics/Events** (pub/sub subjects, event types)
* **Channels** (delivery channels: UI, email, webhook, system log, etc.)
  …and impose **constraints** on naming, immutability, versioning, and compatibility.

---

## 1) Objects that require canonical IDs

Minimum set (extend as needed):

1. **Message ID** (catalog entry identity)
2. **Message Key** (stable lookup key used by code; can be same as ID if you choose)
3. **Event Type / Topic ID** (AsyncAPI-style event name or topic subject)
4. **Channel ID** (delivery channel identity)
5. **Contract ID** (optional but recommended: ties messages/topics to interface contracts)

---

## 2) Canonical grammar (normative)

### 2.1 Common lexical rules (apply to all IDs)

* Character set: `A–Z`, `0–9`, `_`, `-`, `.` (explicitly disallow spaces)
* Case: **UPPERCASE** for tokens; lowercase allowed only for semantic segments if you formalize it (pick one and enforce).
* Separator rules:

  * Use `_` for token boundaries (stable machine parsing)
  * Use `-` inside tokens only when the token is itself a standard label (e.g., `ATA-21`)
  * Use `.` only for hierarchical topic segments (pub/sub)
* Length:

  * Overall ID length ≤ 96 chars
  * Individual token length ≤ 24 chars
* Forbidden:

  * Leading/trailing separators
  * Double separators (`__`, `..`, `--`) unless explicitly reserved
  * Non-ASCII characters

### 2.2 Message ID grammar

**Purpose:** immutable identity for catalog entry and audit.

**EBNF (recommended)**

```
MSG_ID = "MSG" "_" DOMAIN "_" SCOPE "_" CLASS "_" NUM ;
DOMAIN = 1*(ALNUM / "_") ;
SCOPE  = ("ATA-" 2DIGIT) / 1*(ALNUM / "_") ;
CLASS  = "INFO" / "WARN" / "ERR" / "CRIT" ;
NUM    = 4DIGIT ;
```

**Example**

* `MSG_PORTAL_ATA-21_ERR_0042`
* `MSG_CM_ATA-00_WARN_0107`

**Rules**

* `MSG_ID` is immutable once released.
* `NUM` is unique per `{DOMAIN, SCOPE, CLASS}` or per `{DOMAIN, SCOPE}` (pick one and enforce in CI).

### 2.3 Message key grammar (if distinct from Message ID)

**Purpose:** stable developer-facing lookup key; can encode context without the numeric sequence.

```
MSG_KEY = DOMAIN "." SCOPE "." NAME ;
NAME    = 1*(ALNUM / "_" ) ;
```

**Example**

* `portal.ata21.power_insufficient`
* `cm.ata00.schema_violation`

**Rules**

* `MSG_KEY` must be unique globally.
* Renaming a `MSG_KEY` is breaking unless an alias map is maintained.

### 2.4 Event Type / Topic grammar

You want two layers: **event type** (semantic) and **topic/subject** (routing). Keep them related but not identical.

**Event Type (semantic identifier)**

```
EVT_TYPE = DOMAIN "." SCOPE "." ENTITY "." ACTION ".v" MAJOR ;
ENTITY   = 1*(ALNUM / "_" ) ;
ACTION   = 1*(ALNUM / "_" ) ;
MAJOR    = 1*DIGIT ;
```

**Examples**

* `portal.ata21.ecs.requirement_updated.v1`
* `cm.ata00.contract_released.v2`

**Topic/Subject (routing)**

```
TOPIC = ENV "." DOMAIN "." SCOPE "." EVT_FAMILY ;
ENV   = "dev" / "stg" / "prd" ;
EVT_FAMILY = 1*(ALNUM / "_" / ".") ;
```

**Examples**

* `prd.portal.ata21.ecs.requirement_updated`
* `dev.cm.ata00.contract_released`

**Rules**

* Bump `EVT_TYPE` major when payload breaking changes occur.
* Topic naming stays stable across minor changes; include major version in event type to keep routing stable.

### 2.5 Channel ID grammar

Channels represent delivery mechanisms, not semantics.

```
CH_ID = "CH" "_" MEDIUM "_" AUDIENCE "_" SENS ;
MEDIUM   = "UI" / "EMAIL" / "SMS" / "WEBHOOK" / "LOG" / "API" ;
AUDIENCE = "USER" / "ADMIN" / "SYSTEM" / "PARTNER" ;
SENS     = "PUBLIC" / "INTERNAL" / "RESTRICTED" ;
```

**Examples**

* `CH_UI_USER_PUBLIC`
* `CH_WEBHOOK_PARTNER_RESTRICTED`

**Rules**

* Channel IDs are controlled vocabulary; additions require governance approval.

---

## 3) Naming constraints and controlled vocabulary

### 3.1 Controlled vocabularies (minimum)

* `DOMAIN`: e.g., `PORTAL`, `CM`, `CERT`, `OPS`, `MRO` (use your AoR/portal taxonomy if desired)
* `SCOPE`: `ATA-XX` or `CROSS` for cross-ATA
* `CLASS`: `INFO/WARN/ERR/CRIT`
* `MEDIUM/AUDIENCE/SENS`: enumerated list only

### 3.2 Collision rules

* **Global uniqueness** required for:

  * `MSG_ID`
  * `MSG_KEY`
  * `EVT_TYPE`
* **Namespacing** must be enforced via the `DOMAIN` and `SCOPE` tokens.

### 3.3 Immutability rules

Immutable after release:

* `MSG_ID`
* `EVT_TYPE` major (`.v1`, `.v2`, …) is immutable once published
* Topic names in `prd` should be immutable; any change requires parallel publishing for a deprecation window.

Mutable:

* Message text/localization strings (non-breaking if keys/ids unchanged)
* Non-breaking additions to payload schemas (minor version metadata only)

---

## 4) Versioning policy (contracts + messages + events)

### 4.1 Messages

* ID/key stable; content evolves.
* If meaning materially changes, create a **new** `MSG_ID` and deprecate old.

### 4.2 Events / Contracts

* Payload schema versioning aligns to:

  * **Major**: breaking (remove/rename field, change type/meaning)
  * **Minor**: additive optional fields
  * **Patch**: documentation/examples only
* Encode **major** in `EVT_TYPE` (`.vN`) and optionally in schema metadata.

---

## 5) CI-enforceable constraints (Definition of Done)

At minimum, your validator must fail if:

* Any ID violates regex/EBNF rules
* Duplicate `MSG_ID`, `MSG_KEY`, or `EVT_TYPE`
* Any released (tagged) `MSG_ID`/`EVT_TYPE` was modified/renamed
* Event payload breaking change without major bump
* Channel IDs not in controlled vocabulary

---

## 6) Minimal regex set (practical enforcement)

* `MSG_ID`:

  * `^MSG_[A-Z0-9_]+_(ATA-\d{2}|[A-Z0-9_]+)_(INFO|WARN|ERR|CRIT)_\d{4}$`
* `MSG_KEY`:

  * `^[a-z0-9]+(\.[a-z0-9]+)*\.[a-z0-9_]+$`
* `EVT_TYPE`:

  * `^[a-z0-9]+(\.[a-z0-9]+)*\.[a-z0-9_]+\.[a-z0-9_]+\.v[1-9]\d*$`
* `TOPIC`:

  * `^(dev|stg|prd)\.[a-z0-9]+(\.[a-z0-9]+)+$`
* `CH_ID`:

  * `^CH_(UI|EMAIL|SMS|WEBHOOK|LOG|API)_(USER|ADMIN|SYSTEM|PARTNER)_(PUBLIC|INTERNAL|RESTRICTED)$`

---

