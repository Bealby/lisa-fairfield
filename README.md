# ACTRESS - LISA FAIRFIELD

---

The aim of this website is to promote and attract potential casting agents
that are looking for roles in Advertising, Theatre and Film. to give Lisa
Fairfield the opportunity to launch her career in the competitive,
challenging world of acting.

A live version of Website can be found
[here](https://bealby.github.io/Milestone-Project-1/)

## UX

---

Our client desires a website to seek out agents or key contacts, while being 
able to use the Website on business cards and on email signatures. Ultimately
these agents or key contacts in the acting world will lead onto bigger and
greater opportunities with producers and directors. 

### STRATEGY

The main focus of the website is to allure and attract these agents and key
contacts who can open up new doors in a broad range of roles, including
advertising, theatre and films. With the acting market being heavily
competitive, the website needs to stand out from the crowd; be intuitive
in gaining information; while exuding professionalism.

It needs to come across well on mobile devices while users are on the move,
as well as being highly afective on tablets and desktop to allow for a more
comfortable viewing in the office/ home.

Some snippets of user feeback can be find below: 

- ”Producers and directors work under a lot of pressure. Searching for actors/
   actresses will be a ruthless process”

- “Casting agents mainly seek information on: Naturalness, Personality,
   Professionalism, Well-rounded, Training”

- “To have an online presence so that casting directors, producers and
   directors who are interested can learn more about you.”

A graph below illustrates features to implement, valued with importance against viability:

![viabilty-importance-graph](/assets/readme/viability-importance.png/)</div>

### SCOPE

An online presence is fundamental and will be implemented. The client has
provided a montage of photos that will be narrowed down to highlight her different
personalities. A biography of reviews and past and present performances, along with
a ‘blurb’, will be provided by my client. With LisaFairfield being at the start of
her career, show reels/ voice reels are not adequate and hence feasible at this
stage to implement. This should however change as time passes. A blog could also
be a nice little feature to add once my client’s career has taken-off.

The tradeoff in not implementing all desired features mentioned, will not be at
the detriment of the website, as the content we can add will be suffice to kick-start
Lisa Fairfield’s career.

### STRUCTURE

The website needs to be clean and slick without too much clutter and information,
which can cause cognitive overload. It needs to be fresh, stylistic and minimalist
for the artistic audience. At the same time it needs to provide enough content to
promote Lisa Fairfield as an actress. A ‘hero-image’ will be the prominent feature
on the index.html page, alluring potential agents and enticing them to learn more.
The navigation bar and footer will remain fixed through all pages. Alterations will
be madeon the navigation bars in mobile and tablets to maintain the look and feel.

The navigation bar will include tabs for Home, Gallery, Bio, Resume and Contact.
My client’s name will be centered above the navigation bar in clear standout font.
The footer will include a clickable email and telephone number and be viewable in
all pages so that an agent can click intuitively and with ease.

### SKELETON

Please find my Wireframes for Desktop, Tablet and Mobile [here](https://github.com/Bealby/Milestone-Project-1/blob/master/assets/wireframes/lisa-fairfield-wireframes.pdf)

### SURFACE

It is important not to overly glitz-and-glam the website (as the user
may believe), but to keep the website slick and minimal so that is easy for a
potential agent to navigate. I have chosen to use a white color theme with grey
dividers for overall structure. This will allow photos and text to stand out boldly
against the white background, encouraging the desire and ease to navigate fluidly.

## FEATURES

---

The website consists of five separate sections; Home, Gallery, Bio, Resume and
Contact; that are centred between a navigation bar and footer that remain constant
and similar throughout. Keeping to the premise that the name and contact details
are always visable for potential agents.

The website is divided into four separate pages rather than scrolling through one
page. Contrary to current trends, it seemed more fitting for agents, especially
due to the large content of imagery that could potentially overload the Webpage.

Much of the layout of the website used the Bootstrap grid system of containers,
rows and columns; styled by css. This allowed the Website to be clearly structured
and for the content to be responsive.

### FEATURES OF THE WEBSITE

**Header:** A bold, definitive font that can always be clicked to go back to
index.html

**Navigation Bar:** The slick, simplistic navigation bar is initially grey for
each section, turning black (and remaining black) once clicked. The same feature
applies for all other sections, enabling the user to reference where they are on
the Website. Center `mx-auto` was used to centre Nav Bar horizontally.

**Footer:** Lisa Fairfield’s email and phone number are always visible at the
footer of the page. Each is initially grey, but once clicked are highlight black
and directly link to either their email or telephone respectively.

**Sections:**

- **Home:** A striking and bold Hero-Image centred over a white background, nestled
   between the Navbar and Footer.

- **Gallery:** Users are presented with a collage of photos using the Bootstrap
   Grid System.

- **Bio:** A combination of photos and text explaining Lisa’s dreams and desire.
   Including a link to a reference which opens up in a separate page.

- **Resume:** When the Resume is clicked another tab will be opened to display a
  CV in PDF format. This ensures user does not lose their way on the website. This
  is implemented by using `target="_blank"`

- **Contact:** As well as the contact details in the footer a content section was
  also implemented with the use of `<forms>` in bootstrap. This allowes for a more
  user friendly UX in communication and helps keep a record of interest in back-end
  developing.

### FEATURES FOR SMALLER DEVICES

**Tablets:** Some minor features were implemented in the UX for tablets to condense
   the Gallery from three to two columns using the bootstrap function
   of `col-md-6 col-lg-4`.

**Mobile:** It was important to collapse the navigation bar on mobile devices but
  at the same time keep the bold, distint heading. A series of block features were
  used to remove a block divider and keep main header but in a smaller format using
  Bootstrap code `d-none d-sm-block` and `d-block d-sm-none` respectively.
  To reduce the size of the forms in the Contact page the a media query was
  used `@(min-width:992px)`. This allowed for a beter UX in smaller devices.

### FEATURES LEFT TO IMPLEMENT

Below are a list of features I would like to implement in the future which have
not been possible due to the limited content available:

**Blog:** As Lisa's career progresses an added feature would be a blog page
which can be updated on a regular basis

**Form Database:** A feature to enable tabulation of data from potential
clients to create a news update list for Lisa Bealby

**Voice/Show Reels:** An important feature to implement when available
are showreels and voicereels, which will be a crucial featurein
promoting my client

## TECHNOLOGIES USED

---

The following technolgies were used in this project:

- [Balsamiq Wireframes](https://balsamiq.com/wireframes/desktop/) - Allowed
   preliminary designs to be drawn up of Website
- [GitHub](https://github.com/) - Used to store repository and deploy website
- [GitPod](https://gitpod.io/workspaces/) - A platform used for hard coding
   of Website
- [HTML](https://en.wikipedia.org/wiki/HTML) - Markup language of Website
- [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) - Used to style
   HTML elements
- [BOOTSTRAP](https://getbootstrap.com/) - A famework for building responsive
   Websites where the powerful Grid system was used along with styling
- [Google Fonts](https://fonts.google.com/) - Programme used to import main
   fonts in Website: **Playfair Display** and **Calligraffitti**
- [Font Awesome](https://fontawesome.com/) - Programme used to import icons
   for Footer in Website: **far-envelope** and **fas fa-phone**
- [JavaScript](https://www.javascript.com/) - Used in collabration with
   Bootstrap to collaspe Navigation Bar for small devices
- [W3C](https://validator.w3.org/) - Used to validate HTML code
- [WSC](https://jigsaw.w3.org/css-validator/) - Used to validate CSS code
- Popper
- Jquery
- Lint
- Lighthouse Audit

## TESTING

---

## DEPLOYMENT

---

### PUBLISH GitHub REPOSITORY

1.Load up GitHub at <https://github.com>

2.Navigate to the repository titled <https://github.com/Bealby/Milestone-Project-1>

3.Click Settings

4.![Deployment](/assets/readme/deployment-1.png/)

5.Scroll down to:

- Github Pages
- Source
- From drop-down menu choose master branch

6.![Deployment](/assets/readme/deployment-2.png/)

7.From selecting master branch the repository will be refreshed and
   published.
8.Published website will be found highlighted in green under Github Pages
   as below:

![Deployment](/assets/readme/deployment-3.png/)

### CLONE GitHub REPOSITORY

1.Navigate to the repository titled <https://github.com/Bealby/Milestone-Project-1.>.

2.In the main page for the Repository click Clone or Downlaod as shown below.

3.In the main page for the Repository click Clone or Download, then click on
   URL as shown below.

![Deployment](/assets/readme/deployment-4.png/)

4.Open in Terminal

- Change current directory to local directory
- Type `git clone` plus `URL` (copied in step 3). Then `Press Enter`.

## CREDITS

- **Content**
  - The text for section Y was copied from the Wikipedia article Z

- **Media**
  - The photos used in this site were obtained from ...

- **Acknowledgements**
  - I received inspiration for this project from X
