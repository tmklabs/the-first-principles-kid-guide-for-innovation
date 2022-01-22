# **CSS**

describes the visual style of the html content.

Syntax :
Eg :

```
h1 {
font-size:20px;
color : blue;
}
```

<br>

h1 - selector

/_ declaration block starting
{
font-size:20px;
color : blue;
}
/_ declaration block ending

font-size:20px; - declaration or style

font-size - property

20px - value

---

## CSS RULE

```

h1 {
font-size:20px;
color : blue;
}

```

---

WHAT TO LEARN?
<br>

0.  comments

    ```
    /* comment */
    ```

1.  types of css
    inline - using style attribute
    internal - using style element or tag inside head tag.
    external - using a external file with .css extension and using link tag

2.  styling text

        1.font-size
        <br>
        2.font-family - (it wont work unless the user has the font in his system. so we use google fonts cdn)
        <br>

        3.text-transform
        <br>

        4.font-style
        <br>

        5.line-height: 2 (means maintain the gap by taking 2 times the font size)
        <br>

        6.text-align
        <br>

    <hr>

3.  combining selectors : to avoid multiple corrections

    ```
    h1,h2,h3 {
    common styles or declations
    }

    ```

4.  descendant selector
    Eg :

    ```

    header p {
    font-style: italic;
    }

    ```

    Header is a descendant selector or ancestor selector
    and p is a selector

    it means we are apply a common declaration to all the descendant selector (headers) children selectors
    that is p selector.

5.  nested descendant selector : to differentiate form other common selectors

    ```
    article header p {
    font-style: italic;
    }
    ```

    we only want to p tags of header descendant that are of article descendant.

6.  Classes and id's - to avoid too much usage of descendant selectors
    <br>
    **HTML**

    ```
    <header>
        <h2>Article 1</h2>
        <p id="author">Author : aariv</p>
    </header>
    ```

    **CSS**

    ```
    #author {
    color: red;
    }
    ```

    the problem with id is, we cant use the same id for multple selectors

    check this [answer- Why we should not use multiple ids](https://discuss.codecademy.com/t/what-happens-if-we-try-to-apply-the-same-id-to-multiple-elements-will-our-styles-not-get-applied-to-the-targeted-ided-elements/340948/3)

    class - attribute.
    <br>
    **HTML**

    ```
    <header>
        <h2 class="article-style">Article 1</h2>
        <p class="article-style">Author : aariv</p>
    </header>
    ```

    **CSS**

    ```
    .article-style {
    color: red;
    }
    ```

7.  list-style style
8.  colors
    _ RGB
    _ RGBA (a means alpha for transparency)
    _ Hexadecimal notaiton or HEX code
    _ Short hand notation : #ooffbb -> #ofb (must be identical)
    **properties list**
    `1. color tag 2. background-color 3. border`

9.  pseudo classes

        ```
           <ol>
            <li class="first-list">one</li>
            <li>two</li>
            <li>three</li>
          </ol>

           <ul>
            <li class="first-list">one</li>
            <li>two</li>
            <li>three</li>
          </ul>

          .first-list {
             color: rgb(1, 107, 36);
            }

    The other way
    **:first-child : pseudo class**

        ```
        li:first-child{
            color: rgb(1, 107, 36);
        }
        ```

    **NOTE** : mostly we use it for lists. <br>
    some pseudo classes <br>

    1. li:nth-child(even)
    2. li:nth-child(even)
    3. li:nth-child(2)

10. Styling anchor tags

    ```
    a{
        decorations
    }


    a:link
    {
        decorations
    }
     a:visited
    {
        decorations
    }
     a:hover
    {
        decorations
    }
     a:active
    {
        decorations
    }

    text-decoration style


    ```

11. Chrome Developer tools.

12. Confliciting styles/delcrations

    1. id selectors
    2. class selectors (.) or psudo-class selectors (:)
    3. Element selectors
    4. Universal selectors (\*)
    5. in case of multiple selectors
       - last one

13. special case priority

    1. Declarations marked !important
    2. Inline styles

14. Inheritance and Universal selector

    - not every property will undergo inheritance

15. Padding - space inside the element.
16. Margin - space outside the element.
17. final element width : left border + left padding + width + right padding + right border
18. final element height : top broder + top padding + height +
    bottom padding + bottom border
