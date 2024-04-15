LLMs are too good!

I was watching a [video of Geoffrey Hinton](https://www.youtube.com/watch?v=N1TEjTeQeg0) where he is talking about the risks of AI. It's a long video, so after I finished watching the video, I wanted to get a summary of its contents. I first tried to get a transcript of it, but YouTube presents it in a segmented form along with timestamps.

<img width="850" alt="image" src="https://github.com/rangacodes/byte_codes/assets/123901125/b9c4c712-6016-4d31-b159-605fa042c75a">

So I tried inspecting the html of the transcript container to see if I can get the whole transcript as a text block. But the html was very messy. Here's how it looked:

<img width="602" alt="image" src="https://github.com/rangacodes/byte_codes/assets/123901125/f9e52d9a-3cc2-401d-8960-866e66e6d308">

The highlighted text is what I want, but it is dispersed in 321 html segments. So I experimented with ChatGPT to see whether it can help me extract the text from the html code. I got the entire code of the [transcript element](hinton_scary_ai_talk_html.txt) (around 4k lines) and gave it a short sample from it. It was not just able to extract the transcript content perfectly, but it never even needed me to show it how to do so with any examples either.

<img width="562" alt="image" src="https://github.com/rangacodes/byte_codes/assets/123901125/f83eeb0b-55df-444e-af9f-a116ca6a927a">

A contraint on the length of the input limited the amount of content I could extract, and it stopped generating the output after a few hundred lines. So, I asked it to write some Python code to extract the transcript from the html code programmatically. [Code](code_from_llm.py) was perfect, I didn't have to change a thing (except for the input file name). 

After that I got the extracted transcript from the [program output](code_output.txt) and next asked ChatGPT to summarize the key points in the talk. If you have 40 mins, go through the YouTube video, I found it to be very interesting. If you don't have the time, check out the summary [here](summary_from_llm.md)!
