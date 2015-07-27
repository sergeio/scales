Scales
======

Get random scales in your terminal.

```bash
Usage: scales [options] [KEY] ...

Print some scales!

KEY         Starting note of scales.  If omitted, make random.


Options:
  -h, --help            show this help message and exit
  -a, --all-types       Show all supported types of scales.
  -s STYPE, --scale-type=STYPE
                        Selects the type of scale to output.  Default is
                        blues.
```

Example Usage
-------------

Random blues scale:

```bash
$ scales
E♭  F♯  A♭  A  B♭  C♯  E♭
```

Hungarian Minor starting with B-flat:
```bash
$ scales -s hungarian_minor Bb
B♭  C  C♯  E  F  F♯  A  B♭
```


```bash
$ scales
E♭  F♯  A♭  A  B♭  C♯  E♭
```

Show all supported scale types for given starting note:

```bash
$ scales -a C#
major:
C♯  E♭  F  F♯  A♭  B♭  C  C♯
even:
C♯  E♭  F  G  A  B  C♯
blues:
C♯  E  F♯  G  A♭  B  C♯
hungarian_minor:
C♯  E♭  E  G  A♭  A  C  C♯
jazz_minor:
C♯  E♭  E  F♯  A♭  B♭  C  C♯
```
