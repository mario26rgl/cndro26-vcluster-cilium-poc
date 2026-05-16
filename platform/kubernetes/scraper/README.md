# Scraper (concise)

Small scraper pod that polls tenant metrics endpoints from the host cluster. Use it for demos and connectivity checks.

Quick run:
```bash
helm template platform/kubernetes/scraper
kubectl apply -f <rendered.yaml> -n platform-observability --create-namespace
kubectl logs -n platform-observability -l app=platform-scraper -f
```

Configure `targets` and `scrape_interval` in `values.yaml`.
