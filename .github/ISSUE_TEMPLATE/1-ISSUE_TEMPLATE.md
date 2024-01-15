---
name: Compatibility Report
about: Legacy style, everything can be entered in an editable style
title: 'App name [App serial]'
labels: ''
assignees: ''

---

<!-- Please use the game's name for issue Title -->
<!-- issue Title should be "App name [App serial]". App name should be the title of the English version -->
<!-- Amend ? below with the correct information -->

# App summary
- App name: ?
- App serial: ?
- App version: ?

# Vita3K summary
- Version: v?
- Build number: ?
- Commit hash: https://github.com/vita3k/vita3k/commit/[commit] <!-- Replace "[commit]" with commit hash -->
- CPU backend: <!-- As of today Vita3K uses two CPU backend engines to run games: Unicorn and Dynarmic.
                          When testing games Dynarmic should be prefered as it normally gives better results than Unicorn.
                          You can change the CPU backend on the emu settings -->
- GPU backend: <!-- Vita3K has the option to choose bewteen Vulkan and OpenGL,
                          there is no superior option and one can have better results than other -->

# Test environment summary
- Tested by: ?
- OS: Windows/macOS/Linux Distro, Kernel Version? <!-- Please do not submit test results on 
                                                                                         Android as largely different result with PC.
                                                                                         Please submit Android specific issues here
                                                                                         https://github.com/Vita3K/Vita3K-Android/issues -->
- CPU: AMD/Intel?
- GPU: AMD/NVIDIA/Intel?
- RAM: ? GB

# Issues
<!-- Summary of problems -->

# Screenshots
![](https://?)

# Log
<!-- The Vita3K logs are in the same path as the Vita3K itself -->

# Recommended labels
<!-- See https://github.com/Vita3K/compatibility/labels -->
<!-- One of the following status labels must be assigned [Nothing, Bootable, Intro, Menu, Ingame -, Ingame +, Playable] -->
<!-- Watch out for capitalization and typos -->
- A?
- B?
- C?
