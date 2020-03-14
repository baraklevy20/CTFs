# Challenge
The image link appears broken... https://2019shell1.picoctf.com/problem/26832 or http://2019shell1.picoctf.com:26832

# Solution
We open the link and see that once we enter a code, a broken image is shown. We'll try to fix that image, which would probably lead to the flag.

By inspecting the source code we can see that the image is taken from `bytes` endpoint:
```
var bytes = [];
$.get("bytes", function(resp) {
    bytes = Array.from(resp.split(" "), x => Number(x));
});
```

It is then assembled to an image using the following code:
```
function assemble_png(u_in){
    var LEN = 16;
    var key = "0000000000000000";
    var shifter;
    if(u_in.length == LEN){
        key = u_in;
    }
    var result = [];
    for(var i = 0; i < LEN; i++){
        shifter = key.charCodeAt(i) - 48;
        for(var j = 0; j < (bytes.length / LEN); j ++){
            result[(j * LEN) + i] = bytes[(((j + shifter) * LEN) % bytes.length) + i]
        }
    }
    while(result[result.length-1] == 0){
        result = result.slice(0,result.length-1);
    }
    document.getElementById("Area").src = "data:image/png;base64," + btoa(String.fromCharCode.apply(null, new Uint8Array(result)));
    return false;
}
```
We can see that the input has to be of size 16 or we'll use the default key (`0000000000000000`). Then, there's some sort of loop that go through the bytes and put the bytes in a new order in `result`. `result` is then being encoded with a base64 encoding and shown to the screen.

Our goal is to make sure `result` is a valid PNG format, otherwise the image wouldn't be shown.

Every PNG image starts with `137 80 78 71 13 10 26 10`. So the first bytes of `result` has to be that as well.

If we take a look at the code, we can see that `result[0..15]` are calculated when `i=[0..15]` and `j=0`. So for `i=[0..15]` we have (I've replaced shifter with `key` for clarity):
```
result[i] = bytes[(key[i] * LEN) % bytes.length + i]
```
We know for instance that `result[0] = 137`, so we must have that `bytes[(key[0] * LEN) % bytes.length] = 137`. Since `LEN=16` and `key[0]` is possibly a number, the maximum value of `key[0] * LEN` is `16*9=144`, whereas `bytes.length = 704`, so this is equivalent to `bytes[key[0] * 16] = 137`. Therefore to find `key[0]` we can go through the bytes array and find an element that equal `137` whose index is divisible by `16`. In JS we can do so as such:
```
[137, 80, 78, 71, 13, 10, 26, 10].map((ee, j) => (bytes.findIndex((e,i) => e === ee && i % 16 === j) - j) / 16)
```
We get the first 8 digits of our key - 23639114.

By further reading the PNG file format, we can see that the next bytes belong to the `IHDR` chunk. That chunk begins with 4 bytes indicating its length (always 13) and 4 bytes that are equal to `IHDR`. Therefore the next bytes have to be `0, 0, 0, 13, 73, 72, 68, 82` (last 4 values are the ascii values of `IHDR`). We change our function:
```
[137, 80, 78, 71, 13, 10, 26, 10, 0, 0, 0, 13, 73, 72, 68, 82].map((ee, j) => (bytes.findIndex((e,i) => e === ee && i % 16 === j) - j) / 16)
```
And get the full key - `2363911438750653`. By using it a valid image is shown. It's a QR. Once we scan it we get the flag.

Flag: `picoCTF{4c182733af80dd49cc12d13be80d5893}`