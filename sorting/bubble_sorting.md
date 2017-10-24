# Explanation
Compare each item in an array with it's adjacent item.
If the current item is greater than it's adjacent item, swap the two items.
This will put the largest item at the back of the array.
On the next iteration, don't include the last greatest item's index in the search.

## Example found on HackerRank
```   
public static void bubbleSort(int[] x) {
  printArray("Initial", x);

  int endPosition = x.length - 1;
  int swapPosition;

  while( endPosition > 0 ) {
    swapPosition = 0;

    for(int i = 0; i < endPosition; i++) {

    if( x[i] > x[i + 1] ){
      // Swap elements 'i' and 'i + 1':
      int tmp = x[i];
      x[i] = x[i + 1];
      x[i + 1] = tmp;

      swapPosition = i;
      } // end if

      printArray("Current", x);
    } // end for

    endPosition = swapPosition;
  } // end while

  printArray("Sorted", x);
} // end bubbleSort
```













