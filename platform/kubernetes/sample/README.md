# Sample app (concise)

Tiny nginx demo used as a template for tenant workloads. Useful for quick connectivity and network policy tests inside a vCluster.

Quick deploy:
```bash
helm template platform/kubernetes/sample
kubectl apply -f <rendered.yaml> -n sample --create-namespace
```

Edit `values.yaml` to customize image and resources.
