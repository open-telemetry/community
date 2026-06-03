# How to use an Oracle bare metal runner

The Oracle bare metal runner is a shared benchmarking resource. Workflows must
clean up after themselves so they don't fill the shared host filesystem.

## Request access

Access is granted per repository via a community issue. Include:

- The repository that needs access.
- Why the repository needs bare metal resources, such as the benchmark, test
  scenario, or workflow that will use the runner.
- Whether the workflow can run in a job-level container.

All workflows in the repository can use the runner once access is granted.
For the runner label, see
[OpenTelemetry managed assets](../assets.md#bare-metal-runners).

## Prefer job-level containers

Use a job-level container unless the workflow specifically needs direct host OS
access. Containers keep most tool-created temporary files inside the container
filesystem, which reduces the chance that a failed or cancelled job fills the
host `/tmp` directory.

Example:

```yaml
benchmark:
  name: Benchmarks
  runs-on: oracle-bare-metal-64cpu-1024gb-x86-64-ubuntu-24
  container:
    image: golang:1.25-bookworm # use whatever image your workflow needs
  steps:
    - uses: actions/checkout@v5
    - name: Run benchmarks
      run: make benchmark
```

Choose an image that matches the repository's toolchain. For benchmark
stability, prefer a pinned version or digest instead of a moving tag such as
`latest`.

## Clean up when running directly on the host

Some benchmarks need direct host OS access, privileged host features, host
networking, or host-level profiling. If a job must run directly on the host,
route temporary files through `RUNNER_TEMP`, which GitHub Actions empties at
the start and end of every job.

```yaml
benchmark:
  name: Benchmarks
  runs-on: oracle-bare-metal-64cpu-1024gb-x86-64-ubuntu-24
  env:
    TMPDIR: ${{ runner.temp }}
    TMP: ${{ runner.temp }}
    TEMP: ${{ runner.temp }}
  steps:
    - uses: actions/checkout@v5
    - name: Run benchmarks
      run: make benchmark
```

If a tool must write to a fixed path under `/tmp`, add an `if: always()` cleanup
step that removes only the paths created by that job. Do not add broad cleanup
commands such as `rm -rf /tmp/*` or age-based deletion of all `/tmp` files; the
runner may have active control files or other system-managed entries there.

If the runner runs out of space, open a community issue.
