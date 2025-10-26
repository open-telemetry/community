# OpenTelemetry 2025 Governance Committee election

This document lays out the 2025 election process per the OpenTelemetry governance committee [charter document](../../governance-charter.md#eligibility-for-candidacy) requirements.

This election should fill five seats.

Election schedule:

* 17 October 2025 - final deadline to submit nominations
* 20 October 2025 - official nominees list published
* 27 October 2025 to 29 October 2025 - voting takes place
* 31 October 2025 - results announced

We highly encourage participation in this election cycle to ensure that the community is well-represented by the Governance Committee.

# TL;DR

* If you've been nominated or are willing to nominate yourself: check the [charter document](../../governance-charter.md) and confirm you are ready for the commitment. Make sure to provide all necessary information before 17 October 2025 23:59 UTC
* If you are an active community member: confirm that you are on the [voters list](https://github.com/open-telemetry/community/blob/main/elections/2025/voters-roll.csv) or register yourself before 24 October 2025 23:59 UTC.
* Vote between 27 October 2025 ~~00:00~~ 12:00 UTC and end of day 29 October 2025 23:59 via the [voting link](https://github.com/open-telemetry/community/blob/main/elections/2025/governance-committee-election.md)
* Keep being awesome and contributing to the project!

# Vacancies

Current governance committee members (alphabetical order):

- [Alolita Sharma](https://github.com/alolita), Apple, until October 2026
- **[Austin Parker](https://github.com/austinlparker), Honeycomb, until October 2025**
- **[Daniel Gomez Blanco](https://github.com/danielgblanco), New Relic, until October 2025**
- **[Juraci Paixão Kröhling](https://github.com/jpkrohling), OllyGarden, until October 2025**
- [Morgan McLean](https://github.com/mtwo), Splunk, until October 2026
- [Pablo Baeyens Fernandez](https://github.com/mx-psi), Datadog, until October 2026
- **[Severin Neumann](https://github.com/svrnm), Causely, until October 2025**
- **[Ted Young](https://github.com/tedsuo), Grafana Labs, until October 2025**
- [Trask Stalnaker](https://github.com/trask), Microsoft, until October 2026

Five people must be elected in this election, each with two-year terms. Note that five current Governance Committee members end terms as part of this election cycle, though they are welcome to run again for one of the five vacancies.

# Voting process

Anyone can track the 2025 election process via [this GitHub issue](https://github.com/open-telemetry/community/issues/3001). This year's election committee consists of governance committee members Morgan McLean, Trask Stalnaker, and Pablo Baeyens Fernandez. None of whom are up for reelection this year.
We strive for transparency in the election process and hold the community's interests as our priority. In particular, we will ensure that all documents and assets related to the 2025 election process are public, and we will attempt to record and distribute notes for any meetings held as part of this process.

For the 2025 elections, [Helios Voting](https://vote.heliosvoting.org/) was chosen as it's a hosted solution with cryptographic guarantees that no one can meddle with the results. 

Helios Voting also allows us to add GitHub handles to the list of voters in addition to email addresses. We need this, as we count contributions based on GitHub contributions and do not always have the contributor's actual email address. The disadvantage of Helios Voting is that it does not support ranked voting.

The governance committee also evaluated [Condorcet Internet Voting Service](https://civs1.civs.us/) and [Elekto](https://elekto.dev/) but found that they had limitations making Helios Voting a better alternative. Specifically, CIVS [does not have GitHub integration](https://github.com/andrewcmyers/civs/issues/11) and Elekto is beta software with limited contributions, not recommended for production use. We welcome other suggestions for the future.

# Nominations

As per [the charter document](../../governance-charter.md#eligibility-for-candidacy), anybody is eligible to be a nominee for the Governance Committee. During the "call for nomination" period, people can be nominated or nominate themselves by submitting a Pull Request adding said candidate to the [governance-committee-candidates.md](./governance-committee-candidates.md) file in the OpenTelemetry [community](https://github.com/open-telemetry/community) repository. The template in that file includes the following columns:

* Full name
* GitHub alias
* Company affiliation (if applicable)
* Short bio or reasoning to join the Governance Committee (no more than a short paragraph)
* _Optional_: photo/picture of a nominee

The election committee will not merge the Pull Request until the candidate has confirmed their desire to be nominated (if not self-nominating) and has been ratified via PR comments.

Nominees should also send their email address to [cncf-opentelemetry-governance@lists.cncf.io](mailto:cncf-opentelemetry-governance@lists.cncf.io) – it will be kept private and used only for candidate communications as the election process proceeds.

The Governance Committee or appointed people will contact every nominee directly to ensure the commitment and desire to be nominated.

# Voter Eligibility

All [members of standing](../../governance-charter.md#members-of-standing) will automatically be eligible to vote. To confirm your eligibility status, see the [election announcements issue](https://github.com/open-telemetry/community/issues/3001) or the [voter roll](https://github.com/open-telemetry/community/blob/main/elections/2025/voters-roll.csv). If your code contributions do not meet eligibility requirements, but you believe your non-code contributions should make you eligible to vote, you can request an exemption by submitting an exemption [request form](https://docs.google.com/forms/d/e/1FAIpQLSeSA09xDIv0uyb6vrP8xBbLjm8NsgihrG8GHxacbigF17sNDw/viewform?usp=dialog).

One of two options will be available in the form to prove eligibility:

* GitHub handle
* List either:
  * Your contributions to OpenTelemetry that make you eligible to vote, or
  * Your non-code contributions per the [Members of Standing section of the charter](../../governance-charter.md#members-of-standing): particularly, your relationship to a well-known project that's taken a hard dependency on OpenTelemetry, or your involvement with a well-known organization's adoption of OpenTelemetry as an end-user.

All exemption forms are private. Only the current governance and election committee members will have access to this information. The governance committee will discard the lists one month after the election.

# Vote

Everyone with voting rights may log into [Helios Voting](https://vote.heliosvoting.org/helios/elections/f94a7c58-990b-11f0-a16d-5270fb641b4c/view) using their GitHub account. Voting happens through approval voting, where each voter may select up to five candidates. The five candidates with the most votes win the election.

The election committee will accept late registrations to vote and requests to re-send the voting link via email to [cncf-opentelemetry-governance@lists.cncf.io](mailto:cncf-opentelemetry-governance@lists.cncf.io). We encourage pre-registration to minimize the effort required to run this election.

Per Helios Voting, voting is entirely private: nobody will know any individual's vote.

# Results

Voting will close at the end of the day on 29 October 2025 (technically, 23:59 in the International Date Line West time zone / 30 October 2025 noon UTC). Nominees will be stack ranked. If a nominee becomes ineligible (for instance, if more than three topmost nominees work for the same company), the election committee will skip those nominees and pick the nominee with the next-highest score. The exact scores for each candidate will be public.

# Schedule

| Date                      | Activity                                                                                                                                   |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| September 2025            | This document announced                                                                                                                    |
| September 2025            | Election blog post and call for nominations                                                                                                |
| 17 October 2025 23:59 UTC | End of call for nominations                                                                                                                |
| 20 October 2025           | On or before this date Election Committee verifies commitment of all candidates not self-nominated                                         |
| 20 October 2025           | Nominees ratified and pull requests merged on or before this date                                                                          |
| 20 October 2025           | Preliminary list of nominees announced after ratification of all nominees                                                                  |
| 20 October 2025           | List of nominees is finalized on [community](https://github.com/open-telemetry/community) GitHub and advertised via mailing list and Slack |
| 24 October 2025 23:59 UTC | Deadline to apply for a member of standing exemption                                                                                       |
| 27 October 2025 ~~00:00~~ 12:00 UTC | Voting period begins                                                                                                             |
| 30 October 2025 11:59 UTC | Voting ends                                                                                                                               |
| 31 October 2025           | Results are announced                                                                                                                      |
