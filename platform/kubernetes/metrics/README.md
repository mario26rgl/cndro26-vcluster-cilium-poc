# Metrics App Chart

Helm chart for deploying a lightweight Flask-based metrics collection application inside virtual Kubernetes clusters (vClusters). This application exposes system metrics (CPU, memory) via HTTP endpoints.

## Purpose

The metrics app serves as:
1. **Proof-of-concept application** deployed inside vCluster tenants
2. **Observability source** for system-level monitoring (CPU %, memory %)
3. **Cross-cluster scraping target** (polled by [metrics-scraper](../scraper/README.md) from host cluster)
4. **Health check endpoint** for readiness/liveness probes

**Used by**: ArgoCD Application [metrics-app.yaml](../apps/metrics-app.yaml) deployed to `tenant-one` vCluster.

---

## Chart Structure

```
metrics/
```bash
## Verification
| Pod stuck in `Pending` | Resource quota exceeded | Check tenant quotas; reduce `resources.requests` |
# Metrics app (concise)

Lightweight Flask app exposing `/metrics` and `/health`. Intended as a vCluster tenant demo workload and scrape target.

Quick deploy (ArgoCD): ensure `metrics-app` Application is applied and targets the tenant vCluster.

Manual test:
```bash
helm template platform/kubernetes/metrics
kubectl apply -f <rendered.yaml> -n metrics-app --create-namespace
kubectl port-forward -n metrics-app svc/metrics-app 5000:5000
curl http://localhost:5000/metrics
```

Config: change `image` and `resources` in `values.yaml`.
| `resources.requests.cpu` | string | `250m` | CPU request per pod |

