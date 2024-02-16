# compatibility
#### [Commercial game compatibility database for Vita3K.](https://github.com/Vita3K/compatibility/issues)

---
The [Compatibility web page](https://vita3k.org/compatibility.html) fetches data from this repo.

If you want to be a tester and help test games, ask us for write access on our Discord server.

### Note: This repository does **not** guarantee compatibility and is not intended for Android. Submit Android specific issues [here](https://github.com/Vita3K/Vita3K-Android/issues).

### What NOT to post:

  * Non English comments.
  * Tech Support:
    * `How do I do/fix X?`
    * `How do I get games?`
    * `Why won't Vita3K start?`
    * `Why is Vita3K running slow/low FPS?` etc.
  * Begging:
    * `Please fix this/get it working/etc!`
    * `When/how will this be fixed?`
    * `This was my childhood game, please get it working.`
 
These comments will be deleted as soon as we find them.

## Report guidelines:

If you can't find the game issue you want to report, please create a new one.

The following checks are performed by the bot, and those that do not meet will be automatically closed:

- The issue title must be in the format `Game title [Title ID]` (e.g. `Persona 4 Golden [PCSE00120]`).

- commit hash must like this: `Commit hash: https://github.com/vita3k/vita3k/commit/abcd1234` Don't forget to delete `[` and `]`.

- The issue must have a following status label `Nothing, Bootable, Intro, Menu, Ingame -, Ingame +, Playable`.

No checks by bots, but be sure to provide screenshots and logs.

### For testers

You can remove all old labels and give new ones by writing labels under `# Recommended labels` in the issue comment.
