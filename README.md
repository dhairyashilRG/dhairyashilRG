## Dhairyashil R. Ghatage

Performance engineer in Bangalore. I find out where the time, the cost and the failures go in
compilers, parallel code and AI agents, and I publish the measurements so others can re-run them.

Senior Member of Technical Staff at AMD, on the uProf profiler. PhD, Indian Institute of Science (2018).

Website: [dhairyashilrg.dev](https://dhairyashilrg.dev)

### Upstream

Mostly MLIR's vector and affine dialects, plus NVVM lowering.

<!-- PRS:START -->
6 merged, 3 under review. The list updates itself from [the site](https://dhairyashilrg.dev/work).

- [llvm/llvm-project#226517](https://github.com/llvm/llvm-project/pull/226517) [mlir][vector] Add an eliminate-vector-masks pass (open)
- [llvm/llvm-project#226490](https://github.com/llvm/llvm-project/pull/226490) [mlir][linalg] Fix rank-reducing insert_slice vectorization writing to wrong dims (open)
- [llvm/llvm-project#224105](https://github.com/llvm/llvm-project/pull/224105) [MLIR][NVVM] Add SM version requirements to mbarrier Ops (open)
- [llvm/llvm-project#222916](https://github.com/llvm/llvm-project/pull/222916) [MLIR][NVVM] Fix the lowering of legacy mbar.arrive_drop (merged)
- [llvm/llvm-project#221595](https://github.com/llvm/llvm-project/pull/221595) [mlir][vector] Support fixed-size masks in `eliminateVectorMasks` (merged)
- [llvm/llvm-project#219681](https://github.com/llvm/llvm-project/pull/219681) [mlir][vector] Don't fold in_bounds for negative constant indices (merged)
- [llvm/llvm-project#215340](https://github.com/llvm/llvm-project/pull/215340) [mlir][vector] Add a pass to infer the in_bounds attribute (closed, superseded by [#226517](https://github.com/llvm/llvm-project/pull/226517))
- [llvm/llvm-project#214614](https://github.com/llvm/llvm-project/pull/214614) [mlir][affine] Implement ValueBoundsOpInterface for affine.for (merged)
- [llvm/llvm-project#213506](https://github.com/llvm/llvm-project/pull/213506) [mlir][vector] Don't fold in_bounds for scalable vector dimensions (merged)
- [spack/spack-packages#4291](https://github.com/spack/spack-packages/pull/4291) ucx: add external package detection (merged)
<!-- PRS:END -->

Related discussion: [RFC on `in_bounds` versus masking](https://discourse.llvm.org/t/91649), with
measurements across targets. It settled the direction the later patches follow.

### Measurements you can re-run

- [mlir-inbounds-harness](https://github.com/dhairyashilRG/mlir-inbounds-harness): on PolyBench
  `jacobi-2d` (AArch64 NEON), removing the masked loads took `llvm.masked.*` calls from 14 to 0 and
  wall clock from 14.70 to 2.89 ms (median of 21, noise floor 0.45 %). Includes the benchmark,
  the correctness oracle and a write-up of what went wrong on the first attempt
  ([ARTICLE.md](https://github.com/dhairyashilRG/mlir-inbounds-harness/blob/main/ARTICLE.md)).
- [#214614](https://github.com/llvm/llvm-project/pull/214614): loop bounds checked against an
  independent simulation, 12,536 queries with 0 unsound results, plus two mutation controls.
- [#213506](https://github.com/llvm/llvm-project/pull/213506): an out-of-bounds read reproduced
  against a guard page on SVE hardware before the fix.

I use AI coding tools and label them as LLVM's policy asks. Review, testing and responsibility for
every change are mine.

### Background

- **2024 to now, AMD.** C/C++ for the uProf profiler: MPI and OpenMP tracing, and analysis of
  compiler-generated code with the compiler and architecture teams.
- **2018 to 2024, SankhyaSutra Labs.** Built and later led a C++/MPI particle simulator (DSMC),
  2× faster than Sandia's SPARTA on the same hardware in our benchmark, run on 100+ nodes.
- **2011 to 2018, IISc Bangalore.** MSc and PhD on multiscale simulation of fluid flows: molecular
  dynamics in LAMMPS coupled to a continuum solver. Three papers
  ([Google Scholar](https://scholar.google.co.in/citations?user=40V2yM8AAAAJ),
  [ORCID](https://orcid.org/0000-0003-4516-4415)).
- **2007 to 2011, College of Engineering, Pune.** B.Tech.

### Other work

- [agent-harnesses-2026](https://github.com/dhairyashilRG/agent-harnesses-2026): studies of the
  code around AI agents (context, prompt injection, LLM judges, local models), with run ledgers.
- [Cavity2D_BiCGStab_FVM](https://github.com/dhairyashilRG/Cavity2D_BiCGStab_FVM): incompressible
  Navier-Stokes solver with a BiCGStab pressure solve, in C++.
- [SmolLM2_GroundUp](https://github.com/dhairyashilRG/SmolLM2_GroundUp): a small language model
  written from scratch.

### Contact

[hello@dhairyashilrg.dev](mailto:hello@dhairyashilrg.dev) ·
[LinkedIn](https://www.linkedin.com/in/dhairyashilrg)
