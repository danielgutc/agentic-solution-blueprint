# Naming Standard

## Containers

- Use `<system>-<responsibility>` for canonical container names.
- Keep container folder names equal to canonical container names.

## Components

- Do not repeat system name in component names.
- Keep component folder names equal to canonical component names.
- Use `-api` suffix for externally consumed service interfaces.
- Use explicit adapter suffixes such as `-data-access` for persistence/integration roles.
