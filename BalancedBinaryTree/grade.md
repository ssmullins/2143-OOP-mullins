## Program 2 - Binary Tree Balanced Loading
| #       | Item                                                                         | Value       | Earned   |                |
|:--------|:-----------------------------------------------------------------------------|------------:|---------:|:---------------|
| ***1*** | ***General***                                                                |             |          |                |
| -       | Code was on github                                                           | pass/fail   |pass | ![Alt text][1] |
| -       | Code could be ran.                                                           | pass/fail   |pass | ![Alt text][1] |
| -       | Code was commented                                                           |    15       |    15    | ![Alt text][1] |
| -       | Followed naming conventions (named your file correctly).                     |             |          |                |
|         |      Classname: BinarySearch to BalancedSearch                               |    5        |     5    | ![Alt text][1] |
|         |     Foldername: BalancedBinaryTree for all your files.                       |    5        |     5    | ![Alt text][1] |   
|         |     Renamed binary_search_tree_list.py to balanced_binary_tree.py            |    5        |     5    | ![Alt text][1] |
| ***2*** | ***Prompted User***                                                          |             |          |                |
| -       | asked user                                                                   |    10       |    10    | ![Alt text][1] |
| -       | used entered value                                                           |    10       |    10    | ![Alt text][1] |
| ***3*** | ***Balanced Tree***                                                          |             |          |                |
| -       | worked                                                                       |    25       |    5    | ![Alt text][3] |
| ***E*** | ***Added Method***                                                           |             |          |                |
| -       | Added insert method that received an entire list                             |    10       |    10    | ![Alt text][1] |
|         | Totals:                                                                      | **100**     |  **100** | ![Alt text][1] |

### Comments:
- I think you guys misunderstood the "Add Entire List" concept. Your class should get a list (from main, not build it in the class) and insert those values ensuring the tree is balanced.
- You don't ensure (in any way) that the tree will be balanced, you just insert values, then do an in order traversal.
- Basically, most of your `def insertList(self)` method should have been in main, then send the sorted unique list to the class to be worked on.

[1]: http://f.cl.ly/items/3E231i211n2E042B1U3K/right.png  "Correct"
[2]: http://f.cl.ly/items/2X473C1Q1F2x3S1E4231/wrong.gif  "Incorrect"
[3]: http://f.cl.ly/items/1A0d2Q1J1N1u0C3g0C1s/null.gif  "Errors"
