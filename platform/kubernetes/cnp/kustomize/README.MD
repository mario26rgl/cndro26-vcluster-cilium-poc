# CiliumNetworkPolicy Kustomize Overlays

Manages per-scenario CiliumNetworkPolicy manifests for vCluster tenants using Kustomize base + overlays.

## Structure

- `base/` — shared CNP resources (health checks, metrics scraping).
- `overlays/vanilla/` — default scenario (no ClusterMesh enforcement).
- `overlays/clustermesh/` — ClusterMesh-enabled scenario (enforces `io.cilium.k8s.policy.cluster` label in ingress).
- `overlays/mauth/` — mAuth scenario (mutual TLS / identity enforcement).
