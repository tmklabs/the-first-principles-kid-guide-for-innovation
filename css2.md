**LAYOUTS - 3 WAYS TO BUILD**

1. Gives the page a visual structure.
2. The way we arrange the content on a webpage.

two types of layout

1. page layout - the big one or group of component layouts.
2. component layout - the small parts.

3 ways of building layouts

1. Float layouts.

   - Old way of bulding layouts using float css property.
   - outdated

2. Flexbox

   - Modern way of layiing out elements in a 1-Dimensional row without using floats.
   - perfect for component layouts.

3. CSS GRID
   - For layout out element in a fully 2 D grid.
   - perfect for everything.

| Absolute Positioning                                                                            | Float                                                                                                                                      |
| ----------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Element is removed fromnormal flow.                                                             | Element is removed fromnormal flow.                                                                                                        |
| we use top left bottom and right to offset the elemtn from its relatively positioned container. | the container will not adjust its height to the element. you will lose height of the parent if incase you use float on all child elements. |

<br>

4. clearing flaots.
5. box-sizing:border-box property

   - it created exact width.

6. Flexbox
   - flex container
   - flex items

Flexbox is a set of related CSS properties for building 1-dimensional layouts

👉 The main idea behind flexbox is that empty space inside a container element
can be automatically divided by its child elements

👉 Flexbox makes it easy to automatically align items to one another inside a parent container, both horizontally and vertically

👉 Flexbox solves common problems such as vertical centering and creating equal-height columns

👉 Flexbox is perfect for replacing floats,allowing us to write fewer and cleaner HTML and CSS code

7. Flexbox terminology

   - Flex container = display:flex
     - gap: to create space between the item without using margin.
     - justify-content: to aligh items along main axis/horizontal
     - align-items: to aligh items along cross axis/vertically
     - flex-direction : to change the items direction on the main axix/horizonatal
     - flex-wrap: to allow items to wrap into a new line
   - Flex items

     - Main axis
     - Cross Axis
     - aligh-self

     - flex-grow:0
       - specifies how much the item will grow relative to the rest of the flexible items inside the same container.
     - flex-shrink:1
       - shrink or not inside the container. 1 true and 0 false
     - flex-basis:auto
       - specifies the initial length of a flexible item.
     - flex: shorthand (g s b)

     - order: by default its 0, -ve number will arrange the element to the left and the +ve number will take the element to the right.

   - the end
