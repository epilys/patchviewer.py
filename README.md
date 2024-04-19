# `patchviewer.py` [![License]][license]&nbsp;[![No Maintenance Intended]][no-maintenance]

[License]: https://img.shields.io/github/license/epilys/patchviewer.py?color=white
[license]: https://github.com/epilys/patchviewer.py/blob/main/LICENSE
[No Maintenance Intended]: https://img.shields.io/badge/No%20Maintenance%20Intended-%F0%9F%97%99-red
[no-maintenance]: https://unmaintained.tech/

Should be used with a pager with syntax highlighting for `diff` patches like `bat`: `cargo install bat`

## Usage

Download current PR state as a patch series (Format is `mbox` file containing all the commits as email/patches):

If PR url is `https://github.com/org/repo/pull/37`, download:

```url
https://github.com/repo/pull/37.patch
```

as a text file.

```shell
% ./patchviewer.py 37.patch
0 [PATCH 1/4] aaaaaaaa
1 [PATCH 2/4] adkfjslkdfjsdklfj
2 [PATCH 3/4] my hands are typing words
3 [PATCH 4/4] haaaaaaaaands
patches: list
>>> patches[2].view() # launches diff in pager
>>> 
```
