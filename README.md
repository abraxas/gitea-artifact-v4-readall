<p align="center">
  <img src="header.png" alt="Abraxas Labs — gitea-artifact-v4-readall" width="100%">
</p>

<p align="center">
  <a href="https://abraxaslabs.tech"><strong>abraxaslabs.tech</strong></a>
  &nbsp;·&nbsp;
  <a href="https://github.com/abraxas">github.com/abraxas</a>
  &nbsp;·&nbsp;
  <a href="https://x.com/abraxas_null">@abraxas_null</a>
  &nbsp;·&nbsp;
  <a href="https://github.com/abraxas/gitea-artifact-v4-readall">gitea-artifact-v4-readall</a>
</p>

# gitea-artifact-v4-readall

**Gitea** `1.27.3` — Gitea

Unpublished Gitea source finding: artifact v4 unbounded io.ReadAll.

| | |
|---|---|
| ID | Unpublished Gitea source finding #7 (no CVE yet) |
| CWE | [CWE-400](https://cwe.mitre.org/data/definitions/400.html) |
| CVSS | **Medium: 6.5** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:N/I:N/A:H` |
| Product | [Gitea](https://github.com/go-gitea/gitea) |
| Affected | all versions **through 1.27.3** (inclusive) |
| Patched | vendor patch — see references |
| Auth | authenticated (see source map) |
| License | [GNU Affero GPL v3.0](LICENSE) |
| Lab | `127.0.0.1` only · vendor/client disclosure pack, not a scanner |

---

## Advisory (from the source map)

routers/api/actions/artifactsv4.go parseProtobufBody io.ReadAll(ctx.Req.Body) no cap. Contrast job_summary.go io.LimitReader(..., MaxJobSummarySize+1).

---

## Entry

- **Method:** `POST`
- **Path:** `/twirp/github.actions.results.api.v1.ArtifactService/CreateArtifact`
- **Router:** Authenticated Actions job token. parseProtobufBody io.ReadAll with no LimitReader. Contrast job_summary.go io.LimitReader MaxJobSummarySize+1.
- **Notes:** Authenticated unpublished Gitea #7 CWE-400 v1.27.3. Witness: 12 MiB CreateArtifact 200 vs 8 MiB job-summary 400. Not process-kill. Not eval. Not a reverse shell. Fork-PR jobs still need NeedApproval.

### Call chain

- `running Actions job token`
- `POST v4 CreateArtifact 12 MiB → 200 ok + signedUploadUrl`
- `POST job-summary 8 MiB → 400 invalid summary LimitReader`
- `GET /api/v1/version still 200`

### Lab preconditions

- Gitea 1.27.3 with Actions enabled
- Running Actions job token (not a random user PAT)
- Fork-PR jobs still need NeedApproval on 1.27.3

### Witness

12 MiB CreateArtifact HTTP 200 ok; 8 MiB job-summary HTTP 400 invalid summary; Gitea still up

### Not success

- eval/base64/system payload
- reverse shell
- process kill / OOM
- CreateArtifact without a job token

---

## Patch / remediation

**Do this first:** Apply the vendor patch for **Gitea**. See references.

**Verify after upgrade**

- Re-run `gitea-artifact-v4-readall-Abraxas-Labs.py` against the patched build: the mapped witness must **not** appear.
- Confirm the vendor advisory / changeset in the deployed tree (see references).
- A WAF signature is delay, not a patch.

**If you cannot update immediately**

- Disable or isolate the affected component.
- Hunt for the witness condition on production (new privileged users, unexpected files, injected rows — whatever this CVE's map names).

---

## Reproduction (authorized lab)

Target **only** `http://127.0.0.1:8088` (or the loopback you bound). Do not point this script at the internet.

```bash
python3 gitea-artifact-v4-readall-Abraxas-Labs.py
```

Success is the **witness** above in the response body. Generic 200 HTML is not it.

---

## Lab images

Loopback stack used to reproduce. Official images unless a `Dockerfile` in this folder builds from source.

- [`lab/docker-compose.yml`](lab/docker-compose.yml)
- [`lab/Dockerfile`](lab/Dockerfile)
- [`lab/run.sh`](lab/run.sh)

```bash
cd lab
docker compose up --force-recreate
```

Bind the vulnerable product tree next to Compose if the YAML mounts a local directory (plugin zip / source tag from the version table). Publish nothing except `127.0.0.1`.

---

## References

- [github.com/go-gitea/gitea](https://github.com/go-gitea/gitea) tag v1.27.3

- Abraxas Labs: [abraxaslabs.tech](https://abraxaslabs.tech) · [github.com/abraxas](https://github.com/abraxas) · [@abraxas_null](https://x.com/abraxas_null)

---

## Records (structured)

```
# Gitea unpublished #7 — artifact v4 unbounded ReadAll

CWE: CWE-400
Severity: Medium (source review)

## Description

`parseProtobufBody` in artifact v4 does `io.ReadAll(ctx.Req.Body)` with no cap. Job-summary already uses `io.LimitReader` at 1 MiB. A running Actions job token can POST an arbitrarily large CreateArtifact body.

## Product

Gitea 1.27.3. Lab proved the missing cap (12 MiB → 200), not process kill.
```

---

## License

This disclosure pack is licensed under the **GNU Affero General Public License v3.0**. See [LICENSE](LICENSE).

---

## Disclaimer

This pack is for **the vendor, the site owner, and licensed labs**. The script talks to `127.0.0.1`. Using it against systems you do not own is not authorized by Abraxas Labs. No warranty.

<p align="center">
  <a href="https://abraxaslabs.tech">abraxaslabs.tech</a> ·
  <a href="https://github.com/abraxas">github.com/abraxas</a> ·
  <a href="https://x.com/abraxas_null">@abraxas_null</a>
</p>
