# TextAdventure
Interactive story in which a reader can make choices to influence dialogues and the character's behavior

Kivy and KivyMD are required to run the project

The basic idea is to have a text story that has buttons (=choices) from time to time. Choosing one may:
- Result in a change of text only (see screenshots) 
- Result in a change of text AND an impact for the future. For example, if you are within a discussion and you have the choice between "empathic answer" or "rude answer" a variable (e.g. empathy) in the background should increase. Later in the story, if the value is >=3 a different outcome of the story shows up then having a value of <3.

The following requirements are necessary:
- The project should be written with Python
- Kivy is the desired framework
- The story is in German and contains umlauts such as Ü, Ö, Ä
- Each page should be structured according to the 'Text-Buttons' module (meaning a bunch of text will have buttons at the end)
- The number of buttons can vary from 1 to 4
- Buttons lead to the next module. Some buttons only influence the text as described above, while some also increase or decrease a variable in the background. All variables must also be saved in case the app is closed and reloaded when the app is opened again
- Sometimes, there is only one button. If clicked, the value of a specific variable is checked and, depending on the status, one of several paths is selected. Example: In a previous section, the reader could choose between running away from a threat or helping a stranger. Helping a stranger increased the variable "ally". Now this variable is checked. If it's 1 (meaning alive), a text appears in which this ally shows up. If the value is 0 (meaning dead), then another text without this person shows up
- The presentation of the text is a problem and I don't know what makes sense. At the moment the story is in a .docx file. However, it can also be divided into individual chapters and made available in other formats. I've provided some test chapters in the folder chap-sections. The files are in a .txt or .odt
- Very important: When closing and opening the app, the previous module should be loaded. This is to prevent decisions from being undone 


Optional:
- Each page should have a header with "Back to main menu" and the current chapter
- Clicking on the options button in the main menu should have five relevant aspects: 1. dark mode should be selectable as a checkbox, 2. font change for the text, 3. font size change, 4. the changes should be visible in a preview text, 5. Reset of the story and its variables
- In one case, a music file should be played as long as the chapter goes
