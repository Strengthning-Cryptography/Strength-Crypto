# STRENGTHENING CRYPTOGRAPHY USING QUANTUM PROPERTIES

<!--- Mohan { -->
Good Morning to all,

> Intro of ourselfs

Our Project is STRENGTHENING CRYPTOGRAPHY USING QUANTUM PROPERTIES.  
This project is like a proposal to prevent certain rare but possible, vulnerabilities, related to cryptography due to the inability of classical computers to generate true randomness.  

For most of the cryptography algorithms, randomness plays a vital role. But generation of pure random number is impossible in classical computer. Even for generating decent random numbers it needed a random seed. But since the seed is a number in source code or algorithm to generate seed which is also in source, it can be revealed to hacker if the system is compromised. Which made possible to predict all the random numbers the computer will generate by the hacker. So, to solve this issue we introduce quantum computer to create a true randomness using its superposition capability.

<!---  } Me { -->
## No-Cloning 

> Yet to add

## Diffie-Hellman

SO, we successfully found a way to avoid all the problems and to strengthen the cryptography. Server now can benefit from quantum computer,  
but still clients have no access to quantum computers.  
So we started doing some research on finding the algorithm to share true randomness to client, even through an unencrypted channel without any compromise.  
Because if it requires an encrypted channel, then that cryptography algorithm too requires true randomness.  
But luckily we found that the Diffie-Hellman Key Exchange algorithm can be used for this purpose too.  
Now we can share true randomness to clients, so the cryptography is strengthened from both sides.  

<!---  } Pradeish { --->
## System Arch and UML

> Yet to add

<!---  } Me { -->
## Project Demo

SO, For the sake of the project demo we created a CLI based server client chat script which uses all the previously explained techniques.

* Here the server is started.
* It’s loading all the modules including qiskit (which is SDK, for working with the IBM Q quantum processors)
* Now it sends this quantum circuit to IBM Q, and waits for the output..
* It is the random key which is calculated from the results of IBM Q.
* Now it is waiting for the client to connect.
* After the connection has been established, now the pure random key is shared to client using Diffie Hellman Key Exchange.
* Also it uses Digital Signature to avoid man-in-the-middle attack.
* So finally here the client says “Hi” and the server says “Bye”, then both exit.

That's all for Demo

## Future enhancements and Conclusion

> Yet to add

Thank you all for your attention!
