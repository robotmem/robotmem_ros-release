# robotmem_ros

ROS 2 node for [robotmem](https://github.com/robotmem/robotmem) — robot experience memory system.

**Learn once, remember forever, transfer across environments.**

## Packages

| Package | Description |
|---------|-------------|
| `robotmem_ros` | ROS 2 node — 7 Services + 1 Topic + Ready signal |
| `robotmem_msgs` | Message and service definitions (Memory, PerceptionData, NodeStatus) |

## Installation

### From source (colcon)

```bash
# Install robotmem Python package
pip install robotmem

# Clone and build
cd ~/ros2_ws/src
git clone https://github.com/robotmem/robotmem_ros.git
cd ~/ros2_ws
colcon build --packages-select robotmem_msgs robotmem_ros
source install/setup.bash
```

### From apt (coming soon)

```bash
# 1. Install robotmem Python library (pip dependency, not in apt)
pip install robotmem

# 2. Install ROS 2 packages
sudo apt install ros-humble-robotmem-ros ros-humble-robotmem-msgs
```

> **Note:** `robotmem` is a pip-only dependency. The ROS apt packages do not
> automatically pull it in. You must install it separately with `pip install robotmem`.

## Quick Start

```bash
# Launch with defaults
ros2 launch robotmem_ros robotmem.launch.py

# Launch with custom collection
ros2 launch robotmem_ros robotmem.launch.py collection:=robot1

# Launch with namespace (multi-robot)
ros2 launch robotmem_ros robotmem.launch.py ns:=/robot1 collection:=robot1
```

## Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `db_path` | `""` (= `~/.robotmem/memory.db`) | Database file path |
| `collection` | `"default"` | Memory collection name |
| `embed_backend` | `"onnx"` | Embedding backend: `onnx` / `ollama` / `none` |
| `perception_qos` | `"reliable"` | Perception topic QoS: `reliable` / `best_effort` |
| `perception_batch_size` | `50` | Batch size for perception writes |
| `perception_flush_interval` | `1.0` | Flush interval in seconds |

## Services

| Service | Type | Description |
|---------|------|-------------|
| `~/learn` | `Learn` | Record a new experience/insight |
| `~/recall` | `Recall` | Retrieve relevant memories (BM25 + vector hybrid) |
| `~/save_perception` | `SavePerception` | Store perception/trajectory/force data |
| `~/forget` | `Forget` | Mark a memory as superseded |
| `~/update` | `Update` | Modify an existing memory |
| `~/start_session` | `StartSession` | Begin an episode session |
| `~/end_session` | `EndSession` | End session (auto-consolidate + proactive recall) |

## Topics

| Topic | Type | Direction | Description |
|-------|------|-----------|-------------|
| `~/perception` | `PerceptionData` | Subscribe | High-frequency perception stream (batched writes) |
| `~/ready` | `NodeStatus` | Publish | Node health signal (TRANSIENT_LOCAL) |

## Architecture

```
robotmem_ros Node
├── 7 Services (SDK thin wrapper)
│   ├── learn/recall/save_perception  (core API)
│   ├── forget/update                 (memory management)
│   └── start_session/end_session     (episode lifecycle)
├── PerceptionBuffer (batch + seq gap detection + backpressure)
├── CallbackGroups (read/write separation)
│   ├── MutuallyExclusive: write operations
│   ├── Reentrant: recall (read)
│   └── Reentrant: perception stream
└── Ready signal (TRANSIENT_LOCAL QoS)
```

## Supported Distributions

- ROS 2 Humble (Ubuntu 22.04)
- ROS 2 Jazzy (Ubuntu 24.04)
- ROS 2 Rolling

## License

MIT
