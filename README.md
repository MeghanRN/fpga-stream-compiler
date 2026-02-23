# FPGA Stream Compiler

**Deterministic streaming FPGA compilation without writing HDL.**

FPGA Stream Compiler is a domain-specific hardware compiler that converts high-level pipeline intent (YAML or natural language) into validated FPGA implementations. It replaces direct RTL authoring with a constrained intermediate representation (IR) and generates deterministic SystemVerilog using pre-validated templates.

The system is intentionally restricted to deterministic streaming dataflow pipelines to guarantee structural correctness and enforce conservative timing safety margins.

---

## Why This Exists

Traditional FPGA development requires:

* Verilog / SystemVerilog / VHDL expertise
* Timing closure management
* Constraint file authoring (XDC)
* Clock domain discipline
* Vivado / Quartus orchestration

For many small teams building real-time pipelines (sensor filtering, threshold detection, packet manipulation), this complexity is disproportionate.

This compiler constrains the problem space so that:

* Hardware structure is validated before synthesis
* Timing safety margins are enforced automatically
* RTL is generated deterministically
* Toolchain invocation is automated
* LLMs are used only for intent parsing, never for HDL generation

---

## Core Architecture

```
Intent (YAML / Natural Language)
        ↓
Validated Hardware IR
        ↓
Architecture Elaboration
        ↓
Deterministic RTL Templates
        ↓
Constraint Generation
        ↓
Vivado Batch Flow
        ↓
Closed-Loop Timing Adjustment
```

---

## Design Principles

* **LLM is interface-only** — never a generator of record
* **IR is canonical truth**
* **RTL generation is deterministic**
* **Module library is pre-validated**
* **Timing convergence is rule-based and bounded**
* **Constrained domain > general synthesis**

---

## Example (YAML)

```yaml
clock:
  name: clk
  freq_mhz: 50.0

pipeline:
  - op: DigitalInput
    params: { width: 16 }

  - op: Gain
    params: { factor_q: 256 }

  - op: Threshold
    params: { value: 200 }

  - op: DigitalOutput
    params: { width: 1 }
```

---

## Example (Natural Language)

```bash
fpga-compiler \
  --nl "50 MHz pipeline, 16-bit input, gain 1.0, threshold 200, 1-bit output" \
  --board examples/board_artix7.yaml \
  --out build
```

The natural language is converted to structured IR using OpenAI Structured Outputs.
The IR is validated before any hardware is generated.

---

## Features

* Deterministic streaming pipeline model
* Strict IR schema validation
* Automatic pipeline register insertion
* FIFO insertion for buffering boundaries
* Deterministic SystemVerilog generation
* XDC constraint generation
* Vivado batch orchestration
* Rule-based closed-loop timing retry
* IR inspection mode (`--print-ir`)
* Strict parameter enforcement (`--require-explicit`)
* Reproducible IR artifact (`ir.json`)

---

## What This Is Not

This is **not**:

* A general AI hardware generator
* A replacement for RTL engineers in SoC/ASIC design
* A full high-level synthesis (HLS) system
* An arbitrary HDL injection framework

The constraint model is deliberate and foundational.

---

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

---

## Basic Usage

### YAML

```bash
fpga-compiler \
  --pipeline examples/pipeline.yaml \
  --board examples/board_artix7.yaml \
  --out build
```

### Natural Language

```bash
export OPENAI_API_KEY="your_key_here"

fpga-compiler \
  --nl "50 MHz, 16-bit input, gain 1.0, threshold 200, 1-bit output" \
  --board examples/board_artix7.yaml \
  --out build
```

---

## Roadmap

**Current**

* Linear streaming pipelines
* Single clock domain
* Deterministic module set
* Conservative timing stabilization

**Next**

* True DAG support
* FIR filter module
* CDC adapters
* Module characterization database
* Bitstream fingerprinting
* Formal structural checks
* Multi-board support

---

## Status

Early-stage compiler infrastructure for constrained streaming FPGA systems.