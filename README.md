# Linear Cutting Algo

##Description of the cutting algorithm
* The algorithm should check whether it is possible to place the maximum segment from the array of profile segments + gap on a segment of length equal to the length of the whip. If yes, then write this element to the output array of linear cutting results, and delete this, placed segment of the profile from the array of segments waiting for cutting. Then, repeating the action with the remainder of the length of the whip, after placing the previous segment of the profile, you must iterate through the remaining, smaller segments from the array of profiles to be cut. If you manage to place one of them, then you also need to write it to the array of cutting results, remove it from the list of elements to be cut. Repeat this action until we go through all the segments of the profiles. After that, you need to take a new full whip and repeat all these actions again, with the remaining array of profile segments under cutting, for the second and subsequent whips until the segments in the array of profiles to be cut are completely exhausted.

* If the first maximum element cannot be placed on the whole whip, then the algorithm must terminate, yielding an empty array. This means that such a cutting can not be performed, because the required segment of the profile is greater than the length of the whip itself.

* The result of the algorithm working with the input data from the example can be visualized like this:


![Algorithm schema](result.png)


- Size, in conditional units of measurement, the source *whip of the profile material* is one number. Next - *M*.
For example: 5600.
- *A list of segments of a given length* that need to be made from a whip of the material is one array of variable length numbers. Next, *A = [a1, a2, ..., ai, ..., an]*.
For example: [256, 1154, 256, 987, 256, 2200, 1154, 2200, 1154].
An array can be different lengths each time, the values of the array elements can be repeated any number of times.
- The *size of the cut* is one number. Next: *d*.
For example: 4.(not used right now)



##At the output, the function returns:*

* An array of *arrays is the result of a linear cutting operation*, where the elements of the root array are recordings of a string of one whip of the source material, and the contents of the element of this array - an array of segments of the profile of a given length, which managed to be placed on this particular whip. Further *R = [R1, R2, ..., Ri, ..., Rn], where ri = [ri1, ri2, ..., rij, ..., rim]*.
#For example: 
* [[2200, 2200, 1154], [1154, 1154, 987, 256, 256, 256]].
* Processing this output array, it should be possible to calculate and transfer to an external report the number of whips required for cutting a given set of profile segments (root array length), in our case: 2, and a set of numbers rows - a method of cutting a whip (element content root massif.) In our case:
    - 2200, 2200, 1154
    - 1154, 1154, 987, 256, 256, 256
