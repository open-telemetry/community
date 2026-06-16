# OpenTelemetry Storage Semantic Conventions

## Description

As storage systems become increasingly critical to modern infrastructure and cloud-native applications, there is a growing need to standardize observability for storage resources. This project aims to define and stabilize semantic conventions for storage-related telemetry, enabling consistent monitoring and observability across different storage technologies including storage systems, clusters, nodes, pools, arrays, drives, enclosures, volumes, snapshots, volume groups, file systems, and network ports.

This proposal addresses the need for comprehensive storage observability by defining semantic conventions that capture storage infrastructure metrics, resource attributes, and operational characteristics in a vendor-agnostic manner.

### Goals

- Storage users can capture infrastructure metrics and attributes from storage systems with OpenTelemetry and export these to the tools of their choice.
- Storage telemetry includes appropriate resource metadata that conforms to OpenTelemetry semantic conventions, enabling consistent observability across different storage technologies.
- Define semantic conventions for key storage entities including:
  - Storage systems (hardware/software platforms providing data storage)
  - Storage clusters (groups of nodes for high availability and scalability)
  - Storage nodes (individual controllers or servers within storage systems)
  - Storage pools (logical aggregation of storage resources)
  - Storage arrays (disk drives with RAID or data protection)
  - Storage drives (physical storage devices: HDD, SSD, NVMe)
  - Storage enclosures (physical chassis housing drives)
  - Storage volumes (logical storage units presented to hosts)
  - Storage snapshots (point-in-time copies of volumes or file systems)
  - Storage volume groups (collections of volumes managed together)
  - Storage file systems (logical structures organizing files on storage)
  - Storage hosts (servers configured to access storage resources)
  - Storage FC ports (Fibre Channel interfaces for connectivity)
  - Storage IP ports (network interfaces for IP-based protocols)
- Support both block storage and file storage observability use cases.

## Deliverables

- Definition of semantic conventions for storage entities including:
  - **Storage System**: Hardware or software platform providing data storage capabilities
  - **Storage Cluster**: Group of storage nodes working together for high availability and scalability
  - **Storage Node**: Individual controller or server within a storage system or cluster
  - **Storage Pool**: Logical aggregation of storage resources providing unified capacity
  - **Storage Array**: Collection of disk drives configured with RAID or data protection mechanisms
  - **Storage Drive**: Physical storage device (HDD, SSD, NVMe) providing persistent data storage
  - **Storage Enclosure**: Physical chassis housing disk drives with power, cooling, and connectivity
  - **Storage Volume**: Logical unit of storage presented to hosts or applications
  - **Storage Snapshot**: Point-in-time copy of a volume or filesystem capturing data state
  - **Storage Volume Group**: Logical collection of volumes managed together for operations
  - **Storage File System**: Logical data structure organizing and managing files on storage devices
  - **Storage Host**: Server or system configured to access storage resources from a storage system
  - **Storage FC Port**: Physical Fibre Channel interface providing high-speed connectivity
  - **Storage IP Port**: Network interface providing IP-based connectivity for protocols (NFS, SMB, iSCSI)
- Definition of resource attributes for storage entities aligned with existing OpenTelemetry semantic conventions
- Definition of metrics for storage performance, capacity including:
  - IOPS (Input/Output Operations Per Second)
  - Throughput (read/write bandwidth)
  - Latency (response times)
  - Capacity utilization

- Guidelines for mapping vendor-specific storage terminology to standardized semantic conventions
- Documentation of storage topology and relationship modeling (e.g., array → volume → file system)

## Staffing / Help wanted

We welcome contributors from various areas:
- Storage engineers and architects with expertise in enterprise storage systems, SAN/NAS technologies, and cloud storage
- Observability experts familiar with storage monitoring and performance analysis
- Developers working with storage APIs and management interfaces
- Contributors from storage vendors interested in standardizing telemetry
- OpenTelemetry community members interested in infrastructure observability
- Project leads who are willing to drive the project and address any issues which are not handled by other project members
- Sponsoring TC (Technical Committee) members to guide the project through the spec process
- Contributors from Semantic Conventions SIG
- Maintainers or approvers

### Project Leads
To be determined

### Staffing
To be determined

#### GC sponsors
To be determined

#### TC support
The TC is supportive of the storage semantics effort, focusing on:
- Fitting storage telemetry metadata into existing OTel semantic conventions where possible
- Extending conventions only where necessary to capture storage-specific concepts
- Ensuring alignment with existing resource and metric conventions

### Slack Channel
To be created

## Meeting Times
To be determined

## Timeline

### Phase 1: Foundation (Q2 2026)
- Establish working group and define scope
- Review existing storage monitoring practices and identify gaps
- Define core storage entity types and their relationships
- Draft initial semantic conventions for storage arrays and volumes

### Phase 2: Core Conventions (Q3 2026)
- Finalize semantic conventions for primary storage entities (in architectural order):
  - Storage systems (top-level storage platforms)
  - Storage clusters (distributed storage)
  - Storage nodes (individual controllers/servers)
  - Storage pools (logical resource aggregation)
  - Storage enclosures (physical chassis)
  - Storage drives (physical devices)
  - Storage arrays (RAID and data protection)
- Define resource attributes for storage entities
- Define core storage metrics (IOPS, throughput, latency, capacity)

### Phase 3: Extended Conventions (Q4 2026)
- Define semantic conventions for additional storage entities (in architectural order):
  - Storage volumes (logical storage units)
  - Storage snapshots (point-in-time copies)
  - Storage volume groups (collections of volumes)
  - Storage file systems (file organization structures)
  - Storage hosts (servers accessing storage)
  - Storage FC ports (Fibre Channel connectivity)
  - Storage IP ports (IP-based connectivity)
- Document storage topology and relationship modeling

### Phase 4: Integration and Validation (Q1 2027)
- Develop reference implementations and examples
- Validate conventions with storage vendors and users
- Create documentation and best practices guides
- Integrate with OpenTelemetry Collector receivers for storage systems

## Examples: Storage Semantic Conventions

### Storage Entity Types

| **Entity Type** | **Description** | **Key Attributes** |
|----------------|-----------------|-------------------|
| Storage System | Hardware/software platform providing storage | `storage.system.serial_number`, `storage.system.name`, `storage.system.type`, `storage.system.vendor`, `storage.system.model` |
| Storage Cluster | Group of nodes for high availability | `storage.cluster.id`, `storage.cluster.name`, `storage.cluster.domain` |
| Storage Node | Individual controller or server | `storage.node.id`, `storage.node.name`, `storage.node.status`, `storage.node.cluster` |
| Storage Pool | Logical aggregation of storage resources | `storage.pool.id`, `storage.pool.name`, `storage.pool.type`, `storage.pool.status` |
| Storage Enclosure | Physical chassis for drives | `storage.enclosure.id`, `storage.enclosure.serial_number`, `storage.enclosure.type`, `storage.enclosure.power_status` |
| Storage Drive | Physical storage device | `storage.drive.id`, `storage.drive.serial_number`, `storage.drive.vendor`, `storage.drive.model`, `storage.drive.status` |
| Storage Array | Disk drives with RAID/data protection | `storage.array.id`, `storage.array.name`, `storage.array.raid_level`, `storage.array.compressed`, `storage.array.encryption` |
| Storage Volume | Logical storage unit | `storage.volume.id`, `storage.volume.name`, `storage.volume.type`, `storage.volume.status` |
| Storage Snapshot | Point-in-time copy | `storage.snapshot.id`, `storage.snapshot.name`, `storage.snapshot.creation_time`, `storage.snapshot.expire_time` |
| Storage Volume Group | Collection of managed volumes | `storage.volumegroup.id`, `storage.volumegroup.name`, `storage.volumegroup.status` |
| Storage File System | File organization structure | `storage.filesystem.id`, `storage.filesystem.name`, `storage.filesystem.type`, `storage.filesystem.path` |
| Storage Host | Server accessing storage | `storage.host.id`, `storage.host.name`, `storage.host.type`, `storage.host.status` |
| Storage FC Port | Fibre Channel interface | `storage.fc_port.id`, `storage.fc_port.wwpn`, `storage.fc_port.name`, `storage.fc_port.status` |
| Storage IP Port | IP-based network interface | `storage.ip_port.id`, `storage.ip_port.name`, `storage.ip_port.mac_address`, `storage.ip_port.iqn` |

### Metrics Examples

| **Metric** | **Description** | **Unit** | **Attributes** |
|-----------|----------------|---------|---------------|
| `storage.system.io.operations` | Number of I/O operations at system level | `{operations}` | `direction` (read/write), `storage.system.id` |
| `storage.drive.io.operations` | Number of I/O operations per drive | `{operations}` | `direction` (read/write), `storage.drive.id` |
| `storage.drive.io.time` | Time spent on I/O operations | `s` | `direction` (read/write), `storage.drive.id` |
| `storage.volume.io.operations` | Number of I/O operations per volume | `{operations}` | `direction` (read/write), `storage.volume.id` |
| `storage.array.capacity.usage` | Array capacity usage | `By` | `storage.array.id`, `state` (used/available) |
| `storage.volume.capacity.usage` | Volume capacity usage | `By` | `storage.volume.id`, `state` (used/available) |
| `storage.filesystem.usage` | File system space usage | `By` | `storage.filesystem.id`, `state` (used/free/reserved) |
| `storage.filesystem.inodes.usage` | File system inode usage | `{inodes}` | `storage.filesystem.id`, `state` (used/free) |
| `storage.enclosure.temperature` | Enclosure temperature | `Cel` | `storage.enclosure.id` |
| `storage.fc_port.io.operations` | FC port I/O operations | `{operations}` | `direction` (read/write), `storage.fc_port.id` |
| `storage.ip_port.io.operations` | IP port I/O operations | `{operations}` | `direction` (read/write), `storage.ip_port.id` |

### Resource Attributes Examples

| **Attribute** | **Description** | **Example Values** |
|--------------|----------------|-------------------|
| `storage.array.id` | Unique identifier for storage array | `array-001`, `p30da_d` |
| `storage.array.name` | Human-readable name of storage array | `array1`, `production-array` |
| `storage.array.raid_level` | RAID level of the array | `raid0`, `raid1`, `raid5`, `raid6`, `raid10` |
| `storage.array.compressed` | Whether array uses compression | `true`, `false` |
| `storage.array.encryption` | Whether array is encrypted | `true`, `false` |
| `storage.volume.id` | Unique identifier for storage volume | `vol-12345` |
| `storage.volume.name` | Human-readable name of volume | `data-volume-1` |
| `storage.volume.capacity` | Total capacity of volume | `1099511627776` (bytes) |
| `storage.drive.type` | Type of storage drive | `hdd`, `ssd`, `nvme` |
| `storage.cluster.type` | Type of storage cluster | `distributed`, `replicated`, `erasure-coded` |
| `storage.filesystem.type` | File system type | `ext4`, `xfs`, `ntfs`, `zfs` |
| `storage.enclosure.type` | Type of storage enclosure | `jbod`, `das`, `san` |
| `storage.system.type` | Type of storage system | `block`, `file`, `object` |
| `storage.ip_port.address` | IP address of storage port | `192.168.1.100` |

### Use Cases

1. **Storage Performance Monitoring**: Track IOPS, throughput, and latency across storage volumes to identify performance bottlenecks
2. **Capacity Planning**: Monitor storage capacity utilization and growth trends across arrays and volumes
3. **Multi-tier Storage Analysis**: Correlate performance across different storage tiers (SSD, HDD, cloud storage)
4. **Application-Storage Correlation**: Link application performance metrics with underlying storage performance
5. **Storage Topology Visualization**: Map relationships between arrays, volumes, file systems, and applications
6. **Storage Network Monitoring**: Monitor FC and IP port performance and connectivity
7. **Storage Enclosure Monitoring**: Track enclosure health, power, and cooling status

## References

- [Storage Semantic Conventions PR](https://github.com/ramavadl/semantic-conventions/pull/1/files)
- [Metrics Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/general/metrics/)
