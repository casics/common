CASICS Common
================

<img width="100px" align="right" src=".graphics/casics-logo-small.svg">

This is a collection of common utility functions and classes that is included as a submodule by other CASICS modules. Included here are things such as common database access functions, credentials/authentication code, and more.

*Authors*:      [Michael Hucka](http://github.com/mhucka)<br>
*Repository*:   [https://github.com/casics/common](https://github.com/casics/common)<br>
*License*:      Unless otherwise noted, this content is licensed under the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license.

☀ Introduction
-----------------------------

The CASICS code base is modularized into several repositories placed under a [single common organization in GitHub](https://github.com/casics).  Most of the code needs some common utility functions.  To avoid unacceptable copy-pasting of the common routines, we maintain them in this common submodule.

The structure of this module is slightly unusual: it does not have a subdirectory, there is no `setup.py`, and all of the module files are at the top level.  THis makes it possible to incorporate this module in other CASICS modules using `git submodule add`.

⁇ Getting help and support
--------------------------

If you find an issue, please submit it in [the GitHub issue tracker](https://github.com/casics/common/issues) for this repository.

♬ Contributing &mdash; info for developers
------------------------------------------

A lot remains to be done on CASICS in many areas.  We would be happy to receive your help and participation if you are interested.  Please feel free to contact the developers either via GitHub or the mailing list [casics-team@googlegroups.com](casics-team@googlegroups.com).

Everyone is asked to read and respect the [code of conduct](CONDUCT.md) when participating in this project.

❤️ Acknowledgments
------------------

Funding for this and other CASICS work has come from the [National Science Foundation](https://nsf.gov) via grant NSF EAGER #1533792 (Principal Investigator: Michael Hucka).

This incorporates some small functions found in online discussion forums, notably [Stack Overflow](https://stackoverflow.com).  Attributions and links to the original sources are given in the source code here.  According to the posting [Clarity on Using Code on Stack Overflow and Stack Exchange](https://meta.stackexchange.com/questions/271080/the-mit-license-clarity-on-using-code-on-stack-overflow-and-stack-exchange), code contributions on Stack Overflow and Stack Exchange sites is considered to be covered by the [MIT License](https://opensource.org/licenses/MIT) as of February, 2016.
    
<br>
<div align="center">
  <a href="https://www.nsf.gov">
    <img width="105" height="105" src=".graphics/NSF.svg">
  </a>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
  <a href="https://www.caltech.edu">
    <img width="100" height="100" src=".graphics/caltech-round.svg">
  </a>
</div>
