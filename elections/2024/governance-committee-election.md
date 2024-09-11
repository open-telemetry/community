# OpenTelemetry 2024 Governance Committee election

Please see **[the list of candidates running in the election here](./governance-committee-candidates.md)**.

This document lays out the 2024 election process per the OpenTelemetry governance committee [charter document](../../governance-charter.md#eligibility-for-candidacy) requirements.

This election should fill four seats.

Election schedule:

* 11 October 2024 - final deadline to submit nominations
* 14 October 2024 - official nominees list published
* 21 October 2024 to 23 October 2024 - voting takes place
* 25 October 2024 - results announced

We highly encourage participation in this election cycle to ensure that the community is well-represented by the Governance Committee.

# TL;DR

* If you've been nominated or are willing to nominate yourself: check the [charter document](../../governance-charter.md) and confirm you are ready for the commitment. Make sure to provide all necessary information before 11 October 2024 23:59 UTC
* If you are an active community member: confirm that you are on the voters list (see [election announcements issue](https://github.com/open-telemetry/community/issues/2329)) or register yourself before 18 October 2024 23:59 UTC.
* Vote between 21 October 2024 00:00 UTC and 23 October 2024 23:59 UTC via the [voting link](https://vote.heliosvoting.org/helios/elections/176e7ca8-647d-11ef-9b9a-2a30e2a223da/view)
* Keep being awesome and contributing to the project!

# Vacancies

Current governance committee members (alphabetical order):

- [Alolita Sharma](https://github.com/alolita), Apple, until October 2024
- [Austin Parker](https://github.com/austinlparker), Honeycomb, until October 2025
- [Daniel Dyla](https://github.com/dyladan), Dynatrace, until October 2024
- [Daniel Gomez Blanco](https://github.com/danielgblanco), Skyscanner, until October 2025
- [Juraci Paixão Kröhling](https://github.com/jpkrohling), Grafana Labs, until October 2025
- [Morgan McLean](https://github.com/mtwo), Splunk, until October 2024
- [Severin Neumann](https://github.com/svrnm), Cisco, until October 2025
- [Ted Young](https://github.com/tedsuo), Lightstep, until October 2025
- [Trask Stalnaker](https://github.com/trask), Microsoft, until October 2024

Four people must be elected in this election, each with two-year terms. Note that four current Governance Committee members end terms as part of this election cycle, though they are welcome to run again for one of the four vacancies.

# Voting process

Anyone can track the 2024 election process via [this GitHub issue](https://github.com/open-telemetry/community/issues/2329). This year's election committee consists of governance committee members Austin Parker, Daniel Gomez Blanco, and Juraci Paixão Kröhling. None of whom are up for reelection this year.
We strive for transparency in the election process and hold the community's interests as our priority. In particular, we will ensure that all documents and assets related to the 2024 election process are public, and we will attempt to record and distribute notes for any meetings held as part of this process.

For the 2024 elections, [Helios Voting](https://vote.heliosvoting.org/) was chosen as it's a hosted solution with cryptographic guarantees that no GC members can meddle with the results. 

Helios Voting also allows us to add GitHub handles to the list of voters in addition to email addresses. We need this, as we count contributions based on GitHub contributions and do not always have the contributor's actual email address. The disadvantage of Helios Voting is that it does not support ranked voting.

**Note**: there is a current [issue](https://github.com/benadida/helios-server/issues/362) with capitalised GitHub handles and our automatic voter registration process on Helios Voting. We have taken steps to mitigate this issue. However, as an eligible voter, if your GitHub handle contains uppercase characters, and you cannot see yourself as a voter on Helios Voting, please reach out to the election committee at  [cncf-opentelemetry-governance@lists.cncf.io](mailto:cncf-opentelemetry-governance@lists.cncf.io).

The governance committee also evaluated [Condorcet Internet Voting Service](https://civs1.civs.us/) and [Elekto](https://elekto.dev/) but found that they had limitations making Helios Voting a better alternative. Specifically, CIVS [does not have GitHub integration](https://github.com/andrewcmyers/civs/issues/11) and Elekto is beta software with limited contributions, not recommended for production use. We welcome other suggestions for the future.

# Nominations

As per [the charter document](../../governance-charter.md#eligibility-for-candidacy), anybody is eligible to run for the Governance Committee. During the "call for nomination" period, people can be nominated or nominate themselves by submitting a Pull Request adding said candidate to the [governance-committee-candidates.md](./governance-committee-candidates.md) file in the OpenTelemetry [community](https://github.com/open-telemetry/community) repository. The template in that file includes the following columns:

* Full name
* GitHub alias
* Company affiliation (if applicable)
* Short bio or reasoning to join the Governance Committee (no more than a short paragraph)
* _Optional_: photo/picture of a nominee

The election committee will not merge the Pull Request until the candidate has confirmed their desire to be nominated (if not self-nominating) and has been ratified via PR comments.

Nominees should also send their email address to [cncf-opentelemetry-governance@lists.cncf.io](mailto:cncf-opentelemetry-governance@lists.cncf.io) – it will be kept private and used only for candidate communications as the election process proceeds.

The Governance Committee or appointed people will contact every nominee directly to ensure the commitment and desire to be nominated.

# Voter Eligibility

All [members of standing](../../governance-charter.md#members-of-standing) will automatically be eligible to vote. To confirm your eligibility status, see the [election announcements issue](https://github.com/open-telemetry/community/issues/2329). If your code contributions do not meet eligibility requirements, but you believe your non-code contributions should make you eligible to vote, you can request an exemption by submitting an exemption [request form](https://forms.gle/LBvyRpNwZvqcJxUbA).

One of two options will be available in the form to prove eligibility:

* GitHub handle
* List either:
  * Your contributions to OpenTelemetry that make you eligible to vote, or
  * Your non-code contributions per the [Members of Standing section of the charter](../../governance-charter.md#members-of-standing): particularly, your relationship to a well-known project that's taken a hard dependency on OpenTelemetry, or your involvement with a well-known organization's adoption of OpenTelemetry as an end-user.

All exemption forms are private. Only the current governance and election committee members will have access to this information. The governance committee will discard the lists one month after the election.

# Vote

Everyone with voting rights may log into [Helios Voting](https://vote.heliosvoting.org/helios/elections/176e7ca8-647d-11ef-9b9a-2a30e2a223da/view) using their GitHub account. Voting will be approval voting, where each voter may select up to four candidates. The four candidates with the most votes win the election.

The election committee will accept late registrations to vote and requests to re-send the voting link via email to [cncf-opentelemetry-governance@lists.cncf.io](mailto:cncf-opentelemetry-governance@lists.cncf.io). We encourage pre-registration to minimize the effort required to run this election.

Per Helios Voting, voting is entirely private: nobody will know any individual's vote.

# Results

Voting will close on 23 October 2024 at 23:59 UTC. Nominees will be stack ranked. If a nominee becomes ineligible (for instance, if more than three topmost nominees work for the same company), the election committee will skip those nominees and pick the nominee with the next-highest score. The exact scores for each candidate will be public.

# Schedule

| Date                      | Activity                                                                                                                                   |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| August 2024               | This document announced                                                                                                                    |
| August 2024               | Election blog post and call for nominations                                                                                                |
| 11 October 2024 23:59 UTC | End of call for nominations                                                                                                                |
| 14 October 2024           | On or before this date Election Committee verifies commitment of all candidates not self-nominated                                         |
| 14 October 2024           | Nominees ratified and pull requests merged on or before this date                                                                          |
| 14 October 2024           | Preliminary list of nominees announced after ratification of all nominees                                                                  |
| 14 October 2024           | List of nominees is finalized on [community](https://github.com/open-telemetry/community) GitHub and advertised via mailing list and Slack |
| 18 October 2024 23:59 UTC | Deadline to apply for a member of standing exemption                                                                                       |
| 21 October 2024 00:00 UTC | Voting period begins                                                                                                                       |
| 23 October 2024 23:59 UTC | Voting ends                                                                                                                                |
| 25 October 2024           | Results are announced                                                                                                                      |
