<h1>LISA FAIREFILED - ACTRESS</h1>

---

<p>The aim of this website is to promote and attract potential casting agents that are looking for roles 
in Adverts, Theatre and Film. Providing Lisa Fairfield the opportunity to catapult her career in the 
dexterous world of acting.</p>

A live version can be found [here](https://bealby.github.io/Milestone-Project-1/)

<br>

<h1>UX</h1>

---

<p>Our client desires a website to seek out an agent, while being able to use the website on business 
cards and on email signatures. Once an agent is established the ultimate goal would be for it to 
lead to a producer.</p>

<br>

<h3>STRATEGY</h3>

<p>The main focus of the website is to allure and attract potential casting agents and writers 
to seek Lisa Fairfield in a broad range of roles, including adverts, theatre and films. With 
the acting market being heavily competitive, the website needs to stand out from the crowd; be 
intuitive in gaining information; while exuding professionalism.</p>

<p>It needs to work well on mobile devices while users are on the move, as well as working on 
tablets and desktop to allow for a more comfortable viewing in the office/ home.</p>

<br>

- *”Producers and directors work under a lot of pressure. Searching for actors/ actresses will be a 
ruthless process”*

- *“Casting agents mainly seek information on: Naturalness, Personality, Professionalism, 
Well-rounded, Training”*

- *“To have an online presence so that casting directors, producers and directors who are 
interested can learn more about you.”*

<br>

... ![viabilty-importance-graph](/assets/readme/viability-importance.png/)</div>

<br>

<h3>SCOPE</h3>

<p>An online presence is fundamental and will be implemented. The client has provided a montage of
photos that will be narrowed down to highlight her different personalities. A biography of reviews
and past and present performances, along with a ‘blurb’, will be provided by my client. With Lisa 
Fairfield being at the start of her career, show reels/ voice reels are not adequate and hence feasible 
at this stage to implement. This should however change as time passes. A blog could also be a nice little feature 
to add once my client’s career has taken-off.</p>

<p>The tradeoff in not implementing all desired features mentioned, will not be at the detriment of the 
website, as the content we can add will be suffice to kick-start Lisa Fairfield’s career.</p>

<br>

<h3>STRUCTURE</h3>

<p>The website needs to be clean and slick without too much clutter and information, which can cause 
cognitive overload. It needs to be fresh, stylistic and minimalist for the artistic audience.  At 
the same time it needs to provide enough content to promote Lisa Fairfield as an actress. A ‘hero-image’ 
will be the prominent feature on the index.html page, alluring potential agents and enticing them to 
learn more. The navigation bar and footer will remain fixed through all pages. Alterations will be made 
on the navigation bars in mobile and tablets to maintain the look and feel.</p>

<p>The navigation bar will include tabs for Home, Gallery, Bio, Resume and Contact. My client’s name
will be centered above the navigation bar in clear standout font. The footer will include a clickable 
email and telephone number and be viewable in all pages so that an agent can click intuitively and with 
ease.</p>

<br>

<h3>SKELETON</h3>

Please find my Wireframes for Desktop, Tablet and Mobile [here](https://github.com/Bealby/Milestone-Project-1/blob/master/assets/wireframes/wireframes.pdf)

<br>

<h3>SURFACE</h3>

<p>It is important not to overly <i>glitz-and-glam</i> the website (as the user may believe), but to keep the 
website slick and minimal so that is easy for a potential agent to navigate. I have chosen to use a white 
color theme with grey dividers for overall structure. This will allow photos and text to stand out boldly 
against the white background, encouraging the desire and ease to navigate fluidly.</p>

<br>

<h1>FEATURES</h1>

---

<p>The website consists of five separate sections; Home, Gallery, Bio, Resume and Contact; that are centred between 
a navigation bar and footer, that remain constant and similar throughout. This allows the Actress’ name and contact 
details to always be apparent on the webpage no matter where a user is navigating through the website. This keeps to 
the premise that with agents’ time constraints, Lisa Fairfield and her contact details will be the lasting memories 
etched into their minds.</p>

<p>It has been decided not to implement the scrolling feature for all sections to be placed on one continuous page. 
Contrary to current trends, it was felt that with the current quantity of content available, and with the initial main 
desire being to promote Lisa Fairfield from the outset, separate pages for sections seemed more fitting. With the focus 
also being on imagery this may overload the webpage - especially on mobile devices. This can be reassessed again
at a future date.</p>

</p>Much of the layout of the website used the Bootstrap layout feature of containers, rows and columns; styled by css.</p>

**Features of the website:**

**Header:** A bold, definitive font that can always be clicked to go back to index.html

**Navigation Bar:** The slick, simplistic navigation bar is initially grey for each section, turning black (and remaining black) 
once clicked. The same feature applies for all other sections, enabling the user to reference where they are on the website. 
Center `mx-auto` was used to centre horizontally.

**Footer:** Lisa Fairfield’s email and phone number are always visible at the footer of the page. Each is initially grey, but 
once clicked highlight black and directly open either their email or Skype accounts respectively.

**Sections:** 

- **Home:** A striking and bold a Hero-Image centred over a white background nestled between the Navbar and Footer.

- **Gallery:** Users are presented with a collage of photos using bootstrap grid system. Each image is clickable at navigates to source of event website.

- **Bio:** A combination of photos and text explaining Lisa’s dreams and desire. Including her training credentials.

- **Resume:** When the Resume is clicked another tab will be opened to display a CV in PDF format. This ensures user does not lose 
their way on the website. This is implemented by using `target="_blank"`

- **Contact:** As well as the contact details in the footer a content section was also implemented with the use of `<forms>` in bootstrap. 
This allows for a more user friendly UX in communication and helps keep a record of interest back-end developing.

**Features for smaller devices**

**Tablets:** Some minor features were implemented in the UX for tablets to condense the Gallery and Bio section from three to two columns using the bootstrap function of `col-md-6 col-lg-4`.

**Mobile:** It was important to collapse the navigation bar on mobile device but hat the same time keep the bold, distint heading. A series of block features were used remove block divider and keep main header but in smaller format using Bootstrap code `d-none d-sm-block` and `d-block d-sm-none` respecively.
To reduce the size of the forms in the Contact page the follwoing media query was used `@(min-width:992px)`. This allows for a beter UX in smaller devices.

<h3>FEATURES LEFT TO IMPLEMENT</h3>

<p>Below are the list of features I would like to implement in the future which have not been possible in the current website:

**blog** As Lis'a career progress an added feature would be a blog page which can be updated on a regular basis

**Form Database** A feature to enable tabulation of data from potential clients to create a news update list for Lisa Bealby

**Voice/Show Reels** An important feature to implment when avaiulable are showreels and voicereels, which will be a crucial feature to implment.


<br>

<h1>TECHNOLOGIES USED</h1>

---

The following technolgies were used in this project:

- [Balsamiq Wireframes](https://balsamiq.com/wireframes/desktop/)
- [GitHub](https://github.com/)
    - Used to store repository and deply website
- [GitPod](https://gitpod.io/workspaces/)
- [HTML](https://en.wikipedia.org/wiki/HTML)
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
- [BOOTSTRAP](https://getbootstrap.com/)
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [JavaScript](https://www.javascript.com/)
- [W3C](https://validator.w3.org/)
- [WSC](https://jigsaw.w3.org/css-validator/)

<br>


<h1>TESTING</h1>

---


<br>

<h1>DEPLOYMENT</h1>

---

<h3>PUBLISH GitHub REPOSITORY</h3>

1.	Load up GitHub at https://github.com

2.	Navigate to the repository titled https://github.com/Bealby/Milestone-Project-1

3.	Click Settings

![Deployment](/assets/readme/deployment-1.png/)

4.	Scroll down to:

    - Github Pages
    - Source 
    - From drop-down menu choose master branch

![Deployment](/assets/readme/deployment-2.png/)
				
5.	From selecting master branch the repository will be refreshed and published.

6.	Published website will be found highlighted in green under Github Pages as below:

![Deployment](/assets/readme/deployment-3.png/)

<br>

<h3>CLONE GitHub REPOSITORY</h3>

1.	Navigate to the repository titled https://github.com/Bealby/Milestone-Project-1.

2.	In the main page for the Repository click Clone or Downlaod as shown below.

3.	In the main page for the Repository click Clone or Download, then click on URL as shown below.

![Deployment](/assets/readme/deployment-4.png/)

4.	Open in Terminal**

- Change current directory to local directory
- Type `git clone` plus `URL` (copied in step 3). Then `Press Enter`.

<br>

<h1>CREDITS</h1>

- **Content**
    - The text for section Y was copied from the Wikipedia article Z

- **Media**
    - The photos used in this site were obtained from ...

- **Acknowledgements**
    - I received inspiration for this project from X
