# blog.python.cz

[![Build Status](https://travis-ci.org/pyvec/blog.python.cz.svg?branch=master)](https://travis-ci.org/pyvec/blog.python.cz)
[![License Creative Commons](https://img.shields.io/badge/license-CC-000000.svg)](http://creativecommons.org/licenses/by/4.0/)

Source code of the blog of the Czech Python user group. Made for various news, thoughts, and announcements. Written in Czech, but English articles are definitely not prohibited :)

## Simple Writing in 5 steps

Writing a new article can be very simple using just GitHub:

1.  On GitHub, go to the [`content`](https://github.com/pyvec/blog.python.cz/tree/master/content) directory of this repository. Click the <kbd>Create new file</kbd> button in the top right corner.
2.  Name your file in the `YYYY-MM-DD_article-name.md` format, where:

    - `YYYY` is year when the article was published, e.g. `2016`
    - `MM` is month when the article was published, e.g. `08`
    - `DD` is day when the article was published, e.g. `09`
    - `article-name` is dash-separated, lower-cased article title using just ASCII letters/numbers (in other words, no diacritics, please)

    Full example: `2006-08-09_jak-jsem-v-lese-potkal-medveda.md`
3.  Start your article file with following header:

    ```
    Title: Jak jsem v lese potkal medvěda
    Date: 2006-08-09 10:49:00

    ...
    ```

    The time isn't very important.
4.  Then, in place of the three dots `...` you can start writing your article in the [Markdown format](https://guides.github.com/features/mastering-markdown/). You can see how the article will approximately look like using the <kbd>Preview</kbd> tab. Setting <kbd>Soft wrap</kbd> in the top right corner is also handy.
5.  When done with writing, fill the form at the bottom of the page (describe your addition, i.e. "Přidávám článek o medvědovi") and press the <kbd>Propose new file</kbd> button.

## Installation & Advanced Usage

Follow [this user guide](https://github.com/honzajavorek/danube-delta/blob/master/user-guide.rst).

## License

The blog content is licensed under a [Creative Commons Attribution 4.0 International License](http://creativecommons.org/licenses/by/4.0/):

-   Individual articles should be attributed to their respective individual authors.
-   The whole blog as a project should be attributed to the [Pyvec](http://pyvec.org/) nonprofit.

The attached blog software is licensed the same way as the [Danube Delta tool](https://github.com/honzajavorek/danube-delta/blob/master/LICENSE).

All Rights Reserved © 2007–? Honza Javorek &lt;<a
href="mailto:mail&#64;honzajavorek.cz">mail&#64;honzajavorek.cz</a>&gt;
