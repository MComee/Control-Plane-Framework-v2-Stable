# Run Context

This directory is the recursive working-memory plane for constrained model execution.

It is generated from stable project truth and the current run handoff.

## Purpose
- preserve the current run root objective
- decompose recursively through logical levels
- preserve ancestry for every executable node
- keep only bounded execution context active
- retain audit snapshots from previous pass series

## Subdirectories
- `root/` contains the current run root summary
- `tree/` contains recursive node files
- `active/` contains queue and current-node state
- `audit/` contains previous run snapshots
