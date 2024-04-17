# Using actuated

[Actuated](https://actuated.dev/) is available as a GitHub App which can be
enabled on repositories, and allows GH Actions to execute on runners hosted by
the CNCF. [See the announcement](https://actuated.dev/blog/arm-ci-cncf-ampere).

Using actuated is ideal if you need to run an Action on an an ARM64
environment, which GitHub doesn't currently provide.
It should not replace the GitHub Actions runners in every job.

## Installation

Before it can be used, the App has to be enabled on the repository, through a
maintenance request.  [See an
example](https://github.com/open-telemetry/community/issues/1954).

## Usage

Using actuated on a GitHub Actions job consists in changing the `runs-on`
section to be `actuated-arm64-*`, with the required CPUs and RAM in the name.

See the [actuated
documentation](https://docs.actuated.dev/examples/custom-vm-size/) about custom
VM sizes.

For example:

```yaml
runs-on: actuated-arm64-4cpu-16gb
```

This configuration will ensure your job has 4 CPUs and 16GB of RAM available.

While not specifying any CPU/RAM values (`runs-on: actuated-arm64`) currently
works, using that format is deprecated and will be removed.

## Right-sizing VMs

As you set up your job, you may need an estimation of the resources it needs,
to better set your requirements.

Actuated provides VMMeter, a small action which will output system information
at the end of a run.
Follow [the
instructions](https://gist.github.com/alexellis/1f33e581c75e11e161fe613c46180771)
to set it up in your job.

see [the actuated
documentation](https://actuated.dev/blog/right-sizing-vms-github-actions).
