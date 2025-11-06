| Service | SLI                  | SLO cible     | Fenêtre | Méthode de mesure                     | Budget d'erreur |
|---------|----------------------|---------------|---------|----------------------------------------|-----------------|
| API     | Latence p95          | < 300 ms      | 30 j    | Prometheus histogram_quantile         | 0.5%            |
| API     | Taux d'erreur        | < 1%          | 30 j    | rate(5xx)/rate(total)                 | 1%              |
| API     | Disponibilité        | ≥ 99.5%       | 30 j    | uptime probe                          | 0.5%            |
| API     | Saturation CPU       | < 80%         | 30 j    | container_cpu_usage_seconds_total     | —               |