# Asset Loader

Asset Loader is a tool to load the correct version of a standin which can have many variants.

## How to install

You will need some files that several Illogic tools need. You can get them via this link :
https://github.com/Illogicstudios/common

---

## Features

### Visualization

<div align="center">
  <span>
    <img src="https://user-images.githubusercontent.com/94440879/217218731-3f06d164-234a-4ebd-b24d-587efffc80fe.png" width=100%>
  </span>
  <p weight="bold">Visualization of the 3 standins (couch, table and plant)</p>
  <br/>
</div>

We see each standin selected in a table displaying the asset name, the variant name and the version.

<br/>

<div align="center">
  <span>
    <img src="https://user-images.githubusercontent.com/94440879/217219245-1c49df06-04aa-4e49-8991-8e5acec9e612.png" width=75%>
  </span>
  <p weight="bold">Visualization of the variants and versions of the table</p>
  <br/>
</div>

By selecting a standin in the table (or identical standins) the lists on the right display 
the variants and the versions of the selection. The active variant and version are highlighted.

<br/>

### Standin Editing

<div align="center">
  <span>
    <img src="https://user-images.githubusercontent.com/94440879/217220621-052aa855-0bf9-49ba-804d-6521ebb0b8dc.png" width=35%>
  </span>
  <p weight="bold">Buttons to edit the standin</p>
  <br/>
</div>

The 3 buttons "Set Version", "To SD" and "To HD" edit the selected standins :
- Set Version : Set the selected variant and version (on the lists) to the selected standins
- To SD : Find a variant in SD corresponding to the HD variant and version and set it to the selected standins
- To HD : Find a variant in HD corresponding to the SD variant and version and set it to the selected standins

<br/>

<div align="center">
  <span>
    <img src="https://user-images.githubusercontent.com/94440879/217221614-2a8af09a-1318-48e1-89c0-a4fa74dc4fdd.png" width=60%>
  </span>
  <p weight="bold">Standin table with out of date selection</p>
  <br/>
</div>

The button with a warning icon select all the standins that are out of dates. It means that they have an
available higher version of their current variant.

The button "Update to last" set the version of all the selected standins to the last of their variant.

<br/>

### Generation in Maya

<div align="center">
  <span>
    <img src="https://user-images.githubusercontent.com/94440879/217222363-6e29e4da-9c8d-46b3-a4b6-529548699a11.png" width=80%>
  </span>
  <p weight="bold">Buttons in part Generation</p>
  <br/>
</div>

The button "Convert to Maya" hides the selected standins and import the maya objects at the same location
in the DAG and in the scene.

The button "Add transforms" is not implemented yet.
