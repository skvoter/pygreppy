### context:
1. Treewalk and set parents to nodes
2. Find child with pattern. Verify linenumber.
3. Go to top until `codegen.to_source(parent)` length is more than 1
    > **Note**: if Parent is root then add top and bottom sublings. If they are functions or classes - collapse them
4. Get start line number
5. Find end of the parent block (?)
6. Append file[start:end] to results If pattern - `mhighlight()` else `highlight()`
7. Repeat to the end of file
