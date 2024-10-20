SYSTEM_PROMPT = """You are an assistant that is given a note page for a class with a number between 
each paragraph, and new information. Your task is to determine which 
number is the most suitable location in the note page to add the new information. 
Additionally, you must synthesize and rewrite the new information in Github-flavored markdown to fit 
seamlessly into the note's existing content. Return both the number and the rewritten 
new information in markdown, separated by a delimiter '==='. Pay attention to and include necessary 
spacing, punctuation, and symbols for the Github-flavored markdown text."""

EXAMPLE_PROMPT = """Here's an example of the inputs and outputs, ensure your output conforms to the same format.

INPUTS:
Input 1: note page with locations
# Introduction to the Internet
0
## What is the Internet?
1
- **Infrastructure** for transferring data between devices globally
2
- **Not the same** as the World Wide Web
3
  - Web = applications built on top of the Internet (e.g., Facebook, Twitter)
4
  - Other apps use Internet too (e.g., Zoom, online games, IoT devices)
5
## The Internet is Federated
6
- **Federated system**: Requires interoperability between operators
7
- **Challenges**:
8
  - Competing entities forced to cooperate
9
  - Complicates innovation (need common protocols)
10
## Key Considerations
11
1. **Asynchronous operation**
12
   - Data can't move faster than light
13
   - Messages may be outdated upon arrival
14
2. **Designed for failure at scale**
15
   - Multiple components involved in sending a message
16
   - Components can fail without immediate detection


Input 2: new information
Federation enables the tremendous scale of the Internet. Instead of a single operator managing 
billions of users and trillions of services, we only need to focus on interconnecting all the 
different operators. Federation also allows us to build the Internet out of a huge diversity of 
technologies (e.g. wireless, optical), with a huge range of capabilities (e.g. home links with 
tiny capacity, or undersea cables with huge capacity). These technologies are also constantly 
evolving, which means we can't aim for a fixed target (e.g. capacity and demand is constantly 
increasing by orders of magnitude). The massive scale of the Internet also means that any system 
we design has to support the massive range of users and applications on the Internet (e.g. some 
need more capacity than others, some may be malicious).

EXPECTED OUTPUT (do NOT output this portion, just the below line):
10===The Internet is Scalable
- **Enables massive scale**
- Interconnects diverse operators
- Supports various technologies (wireless, optical)
- Adapts to evolving capabilities"""

NOTE_1_CONTENT = """
# Introduction to the Internet

## What is the Internet?
- **Infrastructure** for transferring data between devices globally
- **Not the same** as the World Wide Web
  - Web = applications built on top of the Internet (e.g., Facebook, Twitter)
  - Other apps use Internet too (e.g., Zoom, online games, IoT devices)

## Why is the Internet Interesting?
- **New problem**: Tying together different, existing networks
- **Challenges**:
  - No formal model
  - No measurable performance benchmark
  - Must scale to **billions** of users
  - Must align with business relationships

## The Internet is Federated
- **Federated system**: Requires interoperability between operators
- **Challenges**:
  - Competing entities forced to cooperate
  - Complicates innovation (need common protocols)

## Key Considerations
1. **Asynchronous operation**
   - Data can't move faster than light
   - Messages may be outdated upon arrival
2. **Designed for failure at scale**
   - Multiple components involved in sending a message
   - Components can fail without immediate detection

**Note**: Many Internet design ideas have been adopted in other fields"""

NOTE_2_CONTENT = """
# Router Hardware and Functionality

## What Do Routers Do?

<details>
<summary>Click to expand</summary>

- Routers run routing protocols to populate the forwarding table.
- When a packet arrives, the router:
  1. Examines the destination IP
  2. Uses the forwarding table to select an outgoing link
  3. Forwards the packet along that link

> Note: The forwarding table can contain ranges of addresses.

</details>

## Router Locations

<details>
<summary>Click to expand</summary>

- Small routers: Found in homes and offices
- Large routers: Located in colocation facilities or carrier hotels
  - These are buildings where multiple ISPs install routers to interconnect
  - Specially designed with power and cooling infrastructure
  - ISPs rent space to install routers

Inside a carrier hotel:
```
+-------------------+
|    Router Rack    |
| +---------------+ |
| |    Router 1   | |
| +---------------+ |
| |    Router 2   | |
| +---------------+ |
| |      ...      | |
| +---------------+ |
|  6-7 feet tall    |
|  19 inches wide   |
+-------------------+
```

</details>

## Router Sizes and Capacities

<details>
<summary>Click to expand</summary>

Routers come in various sizes based on user requirements:

| Type | Users | Forwarding Table |
|------|-------|------------------|
| Home | Few | Single default entry |
| Industrial | Thousands | Huge |

### Measuring Router Size

1. Physical size
2. Number of physical ports
3. Bandwidth

Router capacity = Number of physical ports × Bandwidth per port

Example of a modern home router:
```python
ports = [
    {"speed": 100, "count": 4},  # 4 ports at 100 Mbps
    {"speed": 1000, "count": 1}  # 1 port at 1 Gbps
]

total_capacity = sum(p["speed"] * p["count"] for p in ports)
print(f"Total capacity: {total_capacity} Mbps")  # Output: Total capacity: 1400 Mbps
```

### State-of-the-Art ISP Router

- Line rate: Up to 400 Gbps per physical port
- Structure: Multiple removable line cards
  - Each line card contains a set of physical ports
- Example configuration:
  - 8 line cards
  - 36 physical ports per line card
  - Total: 288 physical ports

```python
ports = 288
line_rate = 400  # Gbps
total_capacity = ports * line_rate
print(f"Total capacity: {total_capacity} Gbps ({total_capacity/1000:.1f} Tbps)")
# Output: Total capacity: 115200 Gbps (115.2 Tbps)
```

> Cost: Upwards of $1 million

</details>

## Router Planes

<details>
<summary>Click to expand</summary>

Routers are conceptually divided into three planes:

1. **Data Plane**
   - Main responsibility: Forwarding packets
   - Operates: Locally, without coordinating with other routers
   - Frequency: Every time a packet arrives

2. **Control Plane**
   - Main responsibility: Communicating with other routers and running routing protocols
   - Frequency: When network topology changes (e.g., links added/removed)

3. **Management Plane**
   - Purpose: Configure and monitor the router
   - Users: Systems and human operators
   - Functions:
     - Configuration (e.g., link costs, routing protocols)
     - Monitoring (e.g., traffic volume, hardware failures)

### Comparison of Planes

| Plane | Operation Time Scale | Optimization |
|-------|----------------------|--------------|
| Data | Nanoseconds | Simple tasks (table lookup, forwarding) |
| Control | Seconds | Complex tasks (re-computing network paths) |
| Management | Tens to hundreds of seconds | Configuration and monitoring |

</details>

## Network Management System (NMS)

<details>
<summary>Click to expand</summary>

The NMS is software used by operators to interact with routers:

```mermaid
graph LR
    A[Operator] -->|Uses| B[NMS]
    B -->|Configures| C[Router]
    C -->|Sends telemetry| B
```

- Computes network configuration
- Applies configuration to routers
- Reads telemetry (statistics and running state) from routers

The complexity of the NMS depends on the operator's goals.

</details>
"""

NOTE_3_CONTENT = """# Links and Switches \n Links and switches have limited capacity → 
    how do we share space? We typically **dynamically allocate based on demand**. This is based on 
    the idea that the **peak of aggregate demand is often lower than the aggregate of peak demands**. 
    This approach is much more efficient. Peaks still happen, causing delays or drops, but we tolerate 
    it. Some firms like financial exchanges build their own statically-allocated networks to prevent 
    any delays, and are less sensitive of the cost of doing so. \n ## How do we actually do this dynamic allocation, though? \n - Best effort: everyone sends and see what happens. \n - **Packet 
    switching** does this by forwarding each packet it receives individually, without coordination \n - 
    Reservations: users request bandwidth at start of flow, and release it at end. \n - **Circuit 
    switching** does this by routing at the start and coordinating all routers along a path \n\n Notice 
    both are still statistical multiplexing, just at different granularities. We can define burstiness 
    ($\\frac{\\text{peak usage}}{\\text{{average usage}}}$) as one way to compare the two."""