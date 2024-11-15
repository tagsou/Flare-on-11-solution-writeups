This was my favourite challenge but also the hardest for me although I learnt a ton. 
I realized that the challenge was a based on the [XZ-BACKDOOR](https://www.wired.com/story/xz-backdoor-everything-you-need-to-know/) incident that happened earlier this year. 
We given a copy of a full Linux filesystem. I was abit confused at first but I got hinted by the description that I had to find stolen data (the flag!) and that it had something to do with the **SSH daemon**. 
I applied some basic digital forensics linux techniques and found this ``Flag.txt``

```
⠀⣧⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⣧⠀⠀⠀⢰⡿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡟⡆⠀⠀⣿⡇⢻⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⣿⠀⢰⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡄⢸⠀⢸⣿⡇⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⡇⢸⡄⠸⣿⡇⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⢸⡅⠀⣿⢠⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣥⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⡿⡿⣿⣿⡿⡅⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⠀⠉⡙⢔⠛⣟⢋⠦⢵⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣄⠀⠀⠁⣿⣯⡥⠃⠀⢳⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⡇⠀⠀⠀⠐⠠⠊⢀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⡿⠀⠀⠀⠀⠀⠈⠁⠀⠀⠘⣿⣄⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀
⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣧⠀⠀
⠀⠀⠀⡜⣭⠤⢍⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢛⢭⣗⠀
⠀⠀⠀⠁⠈⠀⠀⣀⠝⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠄⠠⠀⠀⠰⡅
⠀⠀⠀⢀⠀⠀⡀⠡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠔⠠⡕⠀
⠀⠀⠀⠀⣿⣷⣶⠒⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀
⠀⠀⠀⠀⠘⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠊⠉⢆⠀⠀⠀⠀
⠀⢀⠤⠀⠀⢤⣤⣽⣿⣿⣦⣀⢀⡠⢤⡤⠄⠀⠒⠀⠁⠀⠀⠀⢘⠔⠀⠀⠀⠀
⠀⠀⠀⡐⠈⠁⠈⠛⣛⠿⠟⠑⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠑⠒⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
if only it were that easy......

```
If only,lol😂. later I found a **SSHD core dump** file that I thought I need to analzye since it matches the title. 
The coredump file would be really useful in figureing out what caused the crash in the server as it has everything in memory at the time of the crash. 
I opened the coredump in gdb for debugging and found out that a segfault in the coredump was caused by ``/lib/x86_64-linux-gnu/liblzma.so.5``.

I decided to open the liblzma library file in Ghidra and quickly noticed a file that definitely looked like a backdoor. Essentially, what this function does is when ``RSA_public_decrypt gets called`` in ``Opensshd`` it hooks it with its own malicious function.

![Screenshot 2024-11-13 001055](https://github.com/user-attachments/assets/931fb221-ab34-4a10-b647-42582168c049)



Analyzing it more, the function uses a ChaCha20 encryption algorithm to decrypt the encrypted shellcode. In order to tell what shellcode does, we need to decrypt it with the key and nonce. The key and nonce can be found in the coredump.

![liblma backdoor](https://github.com/user-attachments/assets/fe9717de-c39b-44d2-a54d-ddfe8aea824c)


Looking at the function again and looking at the assembly code, we can see the key and nonce should be after this value ``-985630136``  in the coredump. Convert this value to hex ``0xC5407A48``. This is the value we should now look in the coredump(mapped in the coredump).It reads the key (32 bytes) from the 4th offset and the nonce (12 bytes) from the 24th offset.
So all we can do is copy these values from the coredump. 
![chacha20 values](https://github.com/user-attachments/assets/dc6bf02f-ff06-449b-8411-c0029c82aa02)


I used a hex editor for this. Then I copied the encrypted shellcode. 
In Ghidra you can do this by ``highlighting > right-clicking >copy_special>byte_string`` and it should be in your clipboard. 
Then I just use CyberChef to decrypt the shellcode with the ChaCha20 algorithm.

![Screenshot (12)](https://github.com/user-attachments/assets/4b1cf949-5e48-4c5c-8865-90b45347b1af)



loaded the shellcode in Ghidra to reverse it. I noticed a bunch of syscalls, of course. In Ghidra there is a built-in script that can resolve all syscalls.
**ResolveX86orX64LinuxSyscallsScript** that made the shellcode much easier to read.

![image](https://github.com/user-attachments/assets/2b5fff6a-1495-47b5-82c0-b58de83cea79)



The decompiled code isn't 100% correct, but basically what the shellcode does is:

* Establish a remote connection to the attacker's C2 server.
* receives a key by reading 32 bytes
* receives a nonce by reading 12 bytes
* receives a filename
* opens the file and reads it
* strengthens it
* encrypts it with ChaCha20
* Send it back to the attacker's C2 server.



So to decrypt the data, I would first need to find the key, the nonce, and the encrypted data, which would, of course, be in the coredump file.
Looking through the strings of the coredump, I found the filename that was used by the attacker. 
This was a bit of a guess, but it definitely made sense in this case. Now I can find the key and nonce based around the filename offsets.
We know the key and nonce are before the filename, so we just dump 32 bytes (key) and 12 bytes (nonce) from the filename offset. I used gdb for this.

![Screenshot 2024-11-13 170411](https://github.com/user-attachments/assets/956eefc6-2827-4736-959d-b2e4332e57ad)


Now this last part, when trying to decrypt it, really annoyed me, as I first thought the shellcode used a normal ChaCha20 algorithm, but no, I was wrong.
I ditched figuring out how the encryption works and decided to just patch the shellcode's IP address to run locally with a simple Python server.
I did find out however after I solved the challenge that the constant used in the initialization part of the ChaCha20 algorithm, which is ``expand 32-byte K``, used an upper case ``K`` instead of a lower case ``k``, which is usually used in ChaCha20😭😭🧐.


![localhost](https://github.com/user-attachments/assets/bd9747cb-502a-4959-93e2-391bef8ad2e4)

patched the attackers ip address(10.0.2.15:1337) in Ghidra to localhost which is ``0x7f000001`` in hex.

To make the shellcode executable I used this [tool](https://github.com/Njord0/ElfWizard) which made the proccess farely easy. Its basically just a shellcode loader.

then just consulted chatgpt to make me a quick python server to work with the shellcode.I had to change up a few lines but got it working eventually.
now just run the server listening or localhost and the shellcode in sudo and....... FLAG! recived 😎

![Screenshot 2024-11-13 000658](https://github.com/user-attachments/assets/bd816c72-9a92-44ba-b2d9-690e32047f74)
















