# Eval Results

Store iteration results here as `iteration-N/` directories.

Each iteration directory contains:
- `eval-<case-name>/with_skill/outputs/` - outputs with the skill
- `eval-<case-name>/without_skill/outputs/` - baseline outputs
- `eval-<case-name>/eval_metadata.json` - assertions for that case
- `benchmark.json` - aggregated scores for the iteration

Run the viewer with:
```bash
python <skill-creator-path>/eval-viewer/generate_review.py \
  results/iteration-1 \
  --skill-name "presto-design" \
  --benchmark results/iteration-1/benchmark.json
```
