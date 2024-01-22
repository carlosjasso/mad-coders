![logo](../../assets/logo-text.png)

# Challenge: Finding the symmetric difference

### 🤓 A bit of theory

In mathematics, the **[symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference)** of two sets, also known as the **disjunctive union** and **set sum**, is the set of elements which are in either of the sets, but not in their intersection. For example, the symmetric difference of the sets $A = \{1, 2, 3\}$ and $B =\{2, 3, 4\}$ is $A \Delta B = \{1, 4\}$.

The symmetric difference of the sets $A$ and $B$ is commonly denoted by $A \Delta B$, $A \oplus B$, or $A \ominus B$. The calculation of the symmetric difference among more than two sets is a binary operation, which means that the calculation can only be performed between two sets at a time. Therefore, the evaluation of the symmetric difference among three elements ($A \Delta B \Delta C$) is done by one operation at a time. Thus, for the sets $A$ and $B$ defined above, and $C = \{2, 3\}$, $A \Delta B \Delta C = (A \Delta B) \Delta C = \{1, 4\} \Delta \{2, 3\} = \{1, 2, 3, 4\}$.

A visual representation of the symmetric difference of two sets is commonly denoted by the Venn Diagram Theory by

<center>
   <svg
      xmlns:dc="http://purl.org/dc/elements/1.1/"
      xmlns:cc="http://web.resource.org/cc/"
      xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
      xmlns:svg="http://www.w3.org/2000/svg"
      xmlns="http://www.w3.org/2000/svg"
      xmlns:sodipodi="http://inkscape.sourceforge.net/DTD/sodipodi-0.dtd"
      xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
      width="307.28000pt"
      height="223.89000pt"
      id="svg8621"
      sodipodi:version="0.32"
      inkscape:version="0.42.2"
      sodipodi:docbase="C:\Programme\Inkscape"
      sodipodi:docname="Venn0110.svg">
   <defs
      id="defs3" />
   <sodipodi:namedview
      inkscape:document-units="mm"
      id="base"
      pagecolor="#ffffff"
      bordercolor="#666666"
      borderopacity="1.0"
      inkscape:pageopacity="0.0"
      inkscape:pageshadow="2"
      inkscape:zoom="0.66872763"
      inkscape:cx="94.679408"
      inkscape:cy="141.50708"
      inkscape:current-layer="layer1"
      inkscape:window-width="1024"
      inkscape:window-height="742"
      inkscape:window-x="-4"
      inkscape:window-y="-4"
      showborder="true"
      borderlayer="top" />
   <metadata
      id="metadata4">
      <rdf:RDF>
         <cc:Work
            rdf:about="">
         <dc:format>image/svg+xml</dc:format>
         <dc:type
            rdf:resource="http://purl.org/dc/dcmitype/StillImage" />
         </cc:Work>
      </rdf:RDF>
   </metadata>
   <g
      inkscape:label="Layer 1"
      inkscape:groupmode="layer"
      id="layer1">
      <rect
         x="2.5324416"
         y="2.5291228"
         width="379.02979"
         height="274.79257"
         id="rect1310"
         style="fill:#ffffff;fill-opacity:1.0000000;stroke:#000000;stroke-width:5.0498838;stroke-miterlimit:4.0000000;stroke-dasharray:none;stroke-opacity:1.0000000" />
      <circle
         sodipodi:ry="120.00000"
         sodipodi:rx="120.00000"
         sodipodi:cy="180.00000"
         sodipodi:cx="180.00000"
         cx="180.00000"
         cy="180.00000"
         r="120.00000"
         id="circle1312"
         style="fill:#ff0000;fill-opacity:1.0000000;stroke:#000000;stroke-width:6.0000000;stroke-miterlimit:4.0000000;stroke-dasharray:none;stroke-opacity:1.0000000"
         transform="matrix(0.842564,0.000000,0.000000,0.840731,-10.24387,-10.52388)" />
      <circle
         sodipodi:ry="120.00000"
         sodipodi:rx="120.00000"
         sodipodi:cy="180.00000"
         sodipodi:cx="300.00000"
         cx="300.00000"
         cy="180.00000"
         r="120.00000"
         id="circle1316"
         style="fill:#ff0000;fill-opacity:1.0000000;stroke:#000000;stroke-width:6.0000000;stroke-miterlimit:4.0000000;stroke-dasharray:none;stroke-opacity:1.0000000"
         transform="matrix(0.842564,0.000000,0.000000,0.840731,-10.24387,-10.52388)" />
      <path
         d="M 191.97147,53.436405 C 223.25430,71.458270 242.52530,104.76406 242.52530,140.80780 C 242.52530,176.85154 223.25430,210.15733 191.97147,228.17919 C 160.68865,210.15733 141.41763,176.85154 141.41763,140.80780 C 141.41763,104.76406 160.68865,71.458270 191.97147,53.436405"
         id="path1320"
         style="fill:#ffffff;fill-opacity:1.0000000;stroke:#000000;stroke-width:5.0498838;stroke-miterlimit:4.0000000;stroke-dasharray:none;stroke-opacity:1.0000000" />
   </g>
   </svg>
</center>

<div style="page-break-after: always;"></div>

[Here](https://www.youtube.com/watch?v=NPZ3SAJKN1M) you can find a video that explains how the symmetric difference of two sets can be evaluated.

### 📋 The task

Write a function that takes two or more arrays of numbers and returns an array of their symmetric difference. The resulting array must only contain unique values (no duplicates).

*Expected output:*

```js
([1, 2, 3], [2, 3, 4]) => [1, 4];

([1, 2, 3], [2, 3, 4], [2, 3]) => [1, 2, 3, 4];

([1, 2, 3], [4, 5, 6]) => [1, 2, 3, 4, 5, 6];

([0, 0, 1, 1], [1, 1, 2, 2]) => [0, 2];
```

## ⚙ The setup

To execute the challenge code, it's recommended to installl [nodejs](https://nodejs.org/en) on your system. Once installed, you can simply open your terminal into the challenge root directory and run the `npm run start` command to execute your code. You may also run the `npm run test` command for your code to get tested.
