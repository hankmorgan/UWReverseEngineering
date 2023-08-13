# Guide to the Ultima Underworlds

- [Guide to the Ultima Underworlds](#guide-to-the-ultima-underworlds)
  - [Introduction](#introduction)
    - [Contributors](#contributors)
      - [Credits](#credits)
        - [UW-Formats.txt from tthe Abysmal Project](#uw-formatstxt-from-tthe-abysmal-project)
        - [Credits from the Underworld Adventures Prject](#credits-from-the-underworld-adventures-prject)
  - [Terminology and Conventions](#terminology-and-conventions)
  - [Differences Between ``UW1`` and ``UW2``](#differences-between-uw1-and-uw2)
  - [Common Elements between ``UW1`` and ``UW2``](#common-elements-between-uw1-and-uw2)
  - [File Formats](#file-formats)
    - [Files](#files)
    - [Tilemap and Object List](#tilemap-and-object-list)
    - [Player Data](#player-data)
      - [Player Data Overview](#player-data-overview)
      - [``UW1`` *Player.Dat*](#uw1-playerdat)
        - [Decoding and Encoding ``UW1`` *Player.Dat*](#decoding-and-encoding-uw1-playerdat)
        - [``UW1`` *Player.Dat* format](#uw1-playerdat-format)
      - [``UW2`` *Player.Dat*](#uw2-playerdat)
        - [Decoding and Encoding ``UW2`` *Player.Dat*](#decoding-and-encoding-uw2-playerdat)
        - [``UW1`` *Player.Dat* format](#uw1-playerdat-format-1)
    - [Graphic Formats](#graphic-formats)
      - [Textures](#textures)
      - [Sprites](#sprites)
      - [Bitmaps](#bitmaps)
      - [3D Models](#3d-models)
      - [Cutscenes](#cutscenes)
      - [Scheduled Events (*SCD.ARK*)](#scheduled-events-scdark)
  - [Game Mechanics](#game-mechanics)
    - [RNG](#rng)
    - [Attributes](#attributes)
      - [Strength](#strength)
      - [Intelligence](#intelligence)
      - [Dexterity](#dexterity)
      - [Cheat Detection](#cheat-detection)
    - [Skills](#skills)
      - [Skill Checks](#skill-checks)
      - [Specific Skills](#specific-skills)
        - [Attack](#attack)
        - [Defence](#defence)
        - [Unarmed](#unarmed)
        - [Sword, Axe and Mace](#sword-axe-and-mace)
        - [Missile](#missile)
        - [Mana](#mana)
        - [Lore](#lore)
        - [Casting](#casting)
        - [Traps](#traps)
        - [Search](#search)
        - [Track](#track)
          - [Fishing Skill Check](#fishing-skill-check)
      - [Sneak](#sneak)
      - [Repair](#repair)
      - [Charm](#charm)
      - [Lockpick](#lockpick)
      - [Acrobat](#acrobat)
      - [Appraise](#appraise)
      - [Swimming](#swimming)
    - [Combat Mechanics](#combat-mechanics)
    - [Magic](#magic)
      - [Spell List and Effects](#spell-list-and-effects)
      - [Runic Spells](#runic-spells)
      - [Enchanted Items](#enchanted-items)
    - [Survival Mechanics](#survival-mechanics)
      - [Sleeping](#sleeping)
      - [Food](#food)
      - [Death and Resurrection](#death-and-resurrection)
      - [Intoxication](#intoxication)
    - [Game Clock and Time](#game-clock-and-time)
  - [Objects](#objects)
    - [General Object Overview](#general-object-overview)
    - [Special Objects](#special-objects)
      - [Guardian Signet Ring](#guardian-signet-ring)
      - [Data Storage Crystal](#data-storage-crystal)
    - [Traps \& Triggers](#traps--triggers)
      - [Traps](#traps-1)
        - [a\_arrow trap](#a_arrow-trap)
        - [a\_bridge trap](#a_bridge-trap)
        - [a\_change from trap](#a_change-from-trap)
        - [a\_change to trap](#a_change-to-trap)
        - [a\_change terrain trap](#a_change-terrain-trap)
        - [a\_check variable trap](#a_check-variable-trap)
        - [a\_combination trap](#a_combination-trap)
        - [a\_create object trap](#a_create-object-trap)
        - [a\_damage trap](#a_damage-trap)
        - [a\_delete object trap](#a_delete-object-trap)
        - [a\_do trap or a\_hack\_trap](#a_do-trap-or-a_hack_trap)
          - [Camera Trap](#camera-trap)
          - [Platform Trap](#platform-trap)
          - [Trespass Trap](#trespass-trap)
          - [Class Object Trap](#class-object-trap)
          - [Fraznium Forcefield](#fraznium-forcefield)
          - [Unused Oscillating Trap](#unused-oscillating-trap)
          - [Colour Cycling Trap](#colour-cycling-trap)
          - [Ice Floor Collapse Trap](#ice-floor-collapse-trap)
          - [Switch Puzzle Reset Trap](#switch-puzzle-reset-trap)
          - [Platform Puzzle Reset Trap](#platform-puzzle-reset-trap)
          - [Rising Platforms Trap](#rising-platforms-trap)
          - [Loth Tomb Switches](#loth-tomb-switches)
          - [TMAP Change Trap](#tmap-change-trap)
          - [Bullfrog Trap](#bullfrog-trap)
          - [Change Graffiti Trap](#change-graffiti-trap)
          - [Bly Skup Chamber Trap](#bly-skup-chamber-trap)
          - [Scintillus Force Field Trap](#scintillus-force-field-trap)
          - [Change Object Quality Trap](#change-object-quality-trap)
          - [Change TMAP Trap](#change-tmap-trap)
          - [Random Button Flicking Trap](#random-button-flicking-trap)
          - [Avatar is a Coward Trap](#avatar-is-a-coward-trap)
          - [Arena of Fire Safety Trap](#arena-of-fire-safety-trap)
          - [QBert Puzzle Trap.](#qbert-puzzle-trap)
          - [Bottle Recycler Trap](#bottle-recycler-trap)
          - [The Castle Goes Dry Trap](#the-castle-goes-dry-trap)
          - [Light Sphere Recharge Trap](#light-sphere-recharge-trap)
          - [Britannia NPC Teleport](#britannia-npc-teleport)
          - [Unknown Trap 37](#unknown-trap-37)
          - [Spoil Healing Potion Trap](#spoil-healing-potion-trap)
          - [Change Visibility Trap](#change-visibility-trap)
          - [Vending Machine Selection Trap](#vending-machine-selection-trap)
          - [Vending Machine Spawning Trap](#vending-machine-spawning-trap)
          - [Vending Machine Sign Trap](#vending-machine-sign-trap)
          - [A Talking Door!](#a-talking-door)
          - [Change NPC Goal Trap](#change-npc-goal-trap)
          - [Sleep Trap](#sleep-trap)
          - [Unknown Automap Trap](#unknown-automap-trap)
          - [Start Conversation Trap](#start-conversation-trap)
          - [Gem Face Rotate](#gem-face-rotate)
          - [World Teleport Trap](#world-teleport-trap)
          - [Unknown AI Goal Trap 62](#unknown-ai-goal-trap-62)
        - [a\_door trap](#a_door-trap)
        - [a\_flam rune](#a_flam-rune)
        - [a\_jump trap](#a_jump-trap)
        - [a\_null trap](#a_null-trap)
        - [a\_pit trap](#a_pit-trap)
        - [a\_proximity trap](#a_proximity-trap)
        - [a\_set variable trap](#a_set-variable-trap)
        - [a\_skill trap](#a_skill-trap)
        - [a\_special effects trap](#a_special-effects-trap)
        - [a\_spelltrap](#a_spelltrap)
        - [a\_teleport trap](#a_teleport-trap)
        - [a\_text string trap](#a_text-string-trap)
        - [a\_tym rune](#a_tym-rune)
        - [a\_ward trap or a\_tell trap](#a_ward-trap-or-a_tell-trap)
        - [an\_experience trap](#an_experience-trap)
        - [an\_inventory trap](#an_inventory-trap)
        - [an\_oscillator trap](#an_oscillator-trap)
      - [Triggers](#triggers)
        - [a\_close trigger](#a_close-trigger)
        - [a\_look trigger](#a_look-trigger)
        - [a\_move trigger](#a_move-trigger)
        - [a\_pick up trigger](#a_pick-up-trigger)
        - [a\_pressure release trigger](#a_pressure-release-trigger)
        - [a\_pressure trigger](#a_pressure-trigger)
        - [a\_scheduled trigger](#a_scheduled-trigger)
        - [a\_step on trigger](#a_step-on-trigger)
        - [a\_timer trigger](#a_timer-trigger)
        - [a\_use trigger](#a_use-trigger)
        - [an\_enter trigger](#an_enter-trigger)
        - [an\_exit trigger](#an_exit-trigger)
        - [an\_open trigger](#an_open-trigger)
        - [an\_unlock trigger](#an_unlock-trigger)
  - [Quests](#quests)
    - [``UW1`` Quests](#uw1-quests)
    - [``UW2`` Quests](#uw2-quests)
      - [The X Clock](#the-x-clock)
  - [Game worlds and Levels](#game-worlds-and-levels)
    - [``UW1`` Levels](#uw1-levels)
      - [``Tybal's Lair``](#tybals-lair)
      - [The ``Ethereal Void`` Endgame Map](#the-ethereal-void-endgame-map)
    - [``UW2`` Levels](#uw2-levels)
      - [``Brittania``](#brittania)
      - [``Pits Of Carnage``](#pits-of-carnage)
      - [The ``Ethereal Void``](#the-ethereal-void)
        - [QBert Puzzle.](#qbert-puzzle)
  - [NPCS](#npcs)
    - [NPC Basics](#npc-basics)
    - [AI Goals](#ai-goals)
    - [``UW2`` Castle Schedule](#uw2-castle-schedule)
  - [Strings](#strings)
    - [Decoding](#decoding)
    - [String Blocks](#string-blocks)
  - [Conversations](#conversations)
    - [Conversation Machine Code Specification](#conversation-machine-code-specification)
    - [Imported Functions](#imported-functions)
    - [Conversation Variables](#conversation-variables)
  - [Unanswered Questions and Problems](#unanswered-questions-and-problems)
  - [Code Examples](#code-examples)
  - [Reverse Engineering](#reverse-engineering)


## Introduction
This document is a collection of documentation about the file formats and game mechanids for the Ultima Underworld (UW) series of games. 

### Contributors
The information in this document is gathered from a number of sources most notably the vernable uw-formats.txt. Sections of this document if not taken directly from UW-Formats.txt are heavily based on the work that has gone into that document by a number of contributors and groups over the years. Every effort is being made to list this contributions here. To avoid missing anyone I am quoting verbatim the credit section of each copy of uw-formats.txt I can referencing.

#### Credits
##### UW-Formats.txt from tthe Abysmal Project
   My thanks go out to Jim Cameron that started the original "uw-specs.txt"
   file and subsequently found out more unknown data structures and discussed
   about file formats with me. Many thanks, Jim!

   Additional information came from
   Alistair Brown (basic object format, via the Underworld II editor available at
   <http://bearcity.pwp.blueyonder.co.uk/>)
   Ulf Wohlers (Objects and 3D models).
   Fabian Pache (about map details and 3d models, ``UW2`` conversations
   ``UW2`` player save <http://uw2rev.sourceforge.net>).

   Further infos about weapon animation and miscellaneous bits about uw were
   contributed by Telemachos from peroxide.dk.

   I also like to thank Telemachos who pointed me to the TSSHP's file formats
   file at the start of all of this.

   This file is probably:
   Copyright (c) 2008,2009 Julien Langer
   Copyright (c) 2002,2008,2009 Fabian Pache
   Copyright (c) 2000,2001,2002,2003 Jim Cameron
   Copyright (c) 2002,2003,2004 Michael Fink
   Copyright (c) 2004 Kasper Fauerby

##### Credits from the Underworld Adventures Prject
   My thanks go out to Jim Cameron that started the original "uw-specs.txt"
   file and subsequently found out more unknown data structures and discussed
   about file formats with me. Many thanks, Jim!

   Additional information came from Alistair Brown (basic object format, via
   the Underworld II editor available at
   <http://bearcity.pwp.blueyonder.co.uk/>), Ulf Wohlers (Objects and 3D
   models) and Fabian Pache (about map details and 3d models, ``UW2`` related,
   http://uw2rev.sourceforge.net).

   Further infos about weapon animation and miscellaneous bits about uw were
   contributed by Telemachos from peroxide.dk.

   I also like to thank Telemachos who pointed me to the TSSHP's file formats
   file at the start of all of this.

   This file is probably:
   Copyright (c) 2000,2001,2002,2003 Jim Cameron
   Copyright (c) 2002,2003,2004 Michael Fink
   Copyright (c) 2004 Kasper Fauerby



## Terminology and Conventions
``UUW`` - Ultima Underworld, take this to mean both the Underworld games
``UW1`` - Ultima Underworld 1: The Stgygian Abyss.
``UW2`` - Ultima Underworld 2: The Labyrinth of Worlds

Bits fields are referred to as zero based. Eg bit 0 is the first bit in a value.

## Differences Between ``UW1`` and ``UW2``
* ``UW2`` uses a compressed ``lev.ark`` file. 
* ``UW2`` has a different lev.ark block structure.
* ``UW2`` has a scheduled event system controlled by ``*SCD.ARK*`` to allow for more advanced scripting.
* ``UW2`` Cutscenes support scrolling bitmaps.
* ``Do Traps`` in ``UW1`` are renamed ``Hack Traps`` in ``UW2``.
* ``UW2`` has additional terrain types including flowing water and slippery ice.
* ``UW2`` has a different ``*Player.Dat*`` file format.
* ``UW2`` supports more variables and has 3 categories of variable. Quest, Game and X-Clock.
* ``UW2`` has a concept of grouping blocks of 8 levels in to worlds. These worlds may share common hard coded behaviours and events.
* ``UW2`` has additional traps, triggers and conversation functions.
* ``UW2`` handles naming of floor and wall textures differently.

## Common Elements between ``UW1`` and ``UW2``
* Most game mechanics eg combat is the same.
* Object data and property formats are the same
* Tilemap data formats are the same
* Conversation machine code works the same in both games.

## File Formats
### Files
In a typical ``UUW`` installation the following files will be present

TODO: Insert table here. With brief file overview


### Tilemap and Object List

### Player Data
#### Player Data Overview
Player data is stored in ``*Player.Dat*`` files. In both games the data will begin with the player name, attributes, skills and various status bits. 

Then will follow game variables, game state information, player object information(same format as game world objects) and player inventory (same format as game world object lists)


#### ``UW1`` *Player.Dat*
##### Decoding and Encoding ``UW1`` *Player.Dat*

##### ``UW1`` *Player.Dat* format

TODO:


#### ``UW2`` *Player.Dat*
##### Decoding and Encoding ``UW2`` *Player.Dat*

##### ``UW1`` *Player.Dat* format

TODO:



### Graphic Formats
#### Textures

#### Sprites

#### Bitmaps

#### 3D Models

#### Cutscenes

#### Scheduled Events (*SCD.ARK*)

## Game Mechanics
### RNG
RNG is based on the game time that the game has started at.

###  Attributes
#### Strength
``Strength`` is used for the following calculations

Max HP is ``30 + ((Strength * Char Level)/5)``

Max Carry Weight is ``300 + (Strength * 13)``
* Unit 0.1 Stones

Strength controls resistance to intoxication.

#### Intelligence
``Intelligence`` is used for the following calculations

Max Mana is ``((Mana Skill+1)*Int)>>3``

Intelligence controls resistance to hallucination (TO CONFIRM)

#### Dexterity

TODO

#### Cheat Detection
The game will detect that a character has been cheated with if the total attributes score at the end of the game is greater than 100.


### Skills
#### Skill Checks
2 parameters are passed to the skill check function. The skill value and a check difficulty. The difficulty is subtracted from the skill value and a dice roll of 0 to 30 is made and added to give a score value.

The score value is compared to a range of values to give one of 4 skill check results.

|Final Score  |Result           |Return value |
|-------------|-----------------|-------------|
| < 3         |Critical Fail    |  -1         |
| >=4 and<16  |Fail             |   0         |
| >=16 and<=29|Success          |   1         |
| >29         |Critical Success |   2         |


```
score = (skill-difficulty)+ rng (0-30d)

  if (score < 0x1d) {
    if (score < 0x10) {
      if (score < 3) {
         result = -1 ; //0xffff; //critical failure
      }
      else { 
        result = 0;  //failure
      }
    }
    else {
      result = 1; //sucess
    }
  }
  else { //more than 29
    result = 2; //critical sucess
  }
  return result;
```

#### Specific Skills
##### Attack
##### Defence
##### Unarmed
##### Sword, Axe and Mace
##### Missile
##### Mana
Controls the ``mana`` points the player has. Available ``mana`` is the skill multipled by TODO. 

##### Lore
Used for identification of objects. When an object is looked at a skill check of Lore Vs xx is performed and the result stored in the object ``heading`` value.
The ``heading`` bits 0-1 are set with values as follows:

    0 = Unidentified
    1 = Identified as being magical
    2 = Fully identified

Bit 2 is used to track if an identification attempt has been made. Value is set to 1 when the ``lore`` check is attempted. This prevents spamming ``lore`` checks when to brute-force identification. When the ``lore`` skill is increased this value is reset to 0 for all objects in the player inventory to allow re-examination.

##### Casting
Used to perform a skill check whenever the player casts a runic spell. ``Casting`` skill check can have 3 results.
* Critical Success and Success- Spells is cast
* Failure - Spell incantation Failed
* Critical Failure - Spell backfires and applies TODO damage.

TODO How this skillcheck works

##### Traps
Used for disarming traps.

Skill is used when interacting with an object that is linked to a ``Damage Trap``. 

The ``Search`` skill is used to find the traps. To Confirm is this correct?

TODO More detail here and confirm again

##### Search
The ``Search`` skill is evaluated when looking at objects that are linked to a ``Look Trap`` when the look trap has a ??? value set. A skill check is performed against the look skill and if passed the trigger linked to the ``Look Trap`` is executed.


It is also used to detect traps as follows

In ``UW2`` the difficulty of this skill check is based on the ``dungeon_level`` the player is on.

```
World Number = (((dungeon level-1)/8)<<1 + 0xA)
Skill check Result = search skill vs WorldNumber+10
```

TODO confirm how this works in ``UW1``


##### Track
The ``Track`` skill is mainly used to detect if any creatures are located nearby when *F9* is pressed.

TODO More detail on how this works

###### Fishing Skill Check

``Track`` is also used for the skill check value when fishing. If (``Track``+7)/8 > RNG(0-3) then a fish can be caught (assuming there is inventory space).


#### Sneak
To confirm. Compared with a critter object properties value to see if they can become aware of the player. 

#### Repair
Checked when the player performs a ``repair`` on an object using an ``anvil``. Used to evaluation the difficulty message and to calculate the resulting change on object ``quality`` when the ``repair`` is done.

The difficulty estimate of the ``repair`` is based on the items ``durability`` which is used in the below pseudocode to return a string number offset for the estimate. Possible string values trivial (0), simple(1), possible(2), hard(3) and very difficult(4)

```
score = repair - durability + 15d
if (score<0)
  {
    return 0 //trivial
  }
  else
  {
    if (score > 30)
    {
      return 4 //Very Difficult
    }
    else
    {
      return 1 + (score/10) // gives a range of 1 to 3, simple, possible and hard. 
    }
  }
```

When the ``repair`` takes place an addition of time of up to 15 minutes is added to the ``game clock``.
```
RepairTime = ((durability*3)-RepairSkill) - (quality/2)
if (RepairTime>15)
  {
    RepairTime = 15
  }
```

The result of the ``repair`` is a skillcheck of the item ``durability`` vs the ``repair`` skill.

* Critical Success. Item repaired to full ``quality`` (64d)
* Success. ``Quality`` increased by ``3 + ( RepairSkill /5 )``
* Failure. No change is made to the ``quality``
* Critical Failure. A formula is used to calculate the damage. See below

```
if ( rng(0-63) <= quality + RepairSkill )
  {
     Damage =  4 + rng(0-7)
  }
else
  {
    Damage = 0
  }
quality = quality - Damage
```

Final ``Quality`` can be neither less than 0 or greater than 63


#### Charm
No ingame usage but may be used in conversations ``imported functions``. No identified examples of this occuring.

#### Lockpick
Skill is checked when picking a lock using a lockpick. 

The skill check is performed against a value 3 times the ``zpos`` value of any ``a_lock`` object linked to the locked door or chest.

Possible results are
* Critical Success and Success- Door is unlocked
* Failure - Door remains locked
* Critical Failure - Door remains locked. Another skill check of ``Dexterity`` vs 20d takes place. If this fails the lockpick is broken.



#### Acrobat
Checked when the player lands after jumping or falling from a height. Skill check is performed against value TODO (To confirm was this the velocity at landing?)

Checked when standing on an unstable ice tile to see if the ice tile will collapse. See the Hack Trap/Ice Collapse Trap for details.




To Confirm - Does this skill have an impact on jump distance

To confirm - is there skill check critical results

#### Appraise
Use to evaluate the trade deal being currently offered in bartering
Sums the value of the items being offered to and by the player. A skill check is tested against TODO and based on the sucess or failure the appropiate trade evaluation message is displayed

#### Swimming
Use to control swimming speed(to confirm) and once a minute(to confirm) a skill check is performed against the ``swimming`` skill. 

The skill check is based on the carried and max ``weight`` encumberance of the player.
``Check Difficulty = ((Carried weight<<5)/(Max Weight))``
Depending on the check result 

If the skill check fails damage is applied based on the possible fail values of 0 or -1 using a damage roll using a D4 dice.

``Damage = (3 - CheckResult)D4``
ie 
3D4 or 4D4 damage is applied.

### Combat Mechanics

### Magic

#### Spell List and Effects

#### Runic Spells

#### Enchanted Items


### Survival Mechanics
#### Sleeping

#### Food

#### Death and Resurrection

#### Intoxication

### Game Clock and Time


## Objects

### General Object Overview

### Special Objects
A summary of some objects with special behaviours

#### Guardian Signet Ring
The guardian signet ring when invisible is used to mark a place of power for the wand of Altara spell.

#### Data Storage Crystal
The text on the data crystal is set based on the crystal ``quality``.
It can be observed to have the following properties for each character. Starting with label *Q6Y6* at ``quality`` 0 for incrementing ``quality`` values.

* Char 0 - letters goes down by 2 each time
* Char 1 - decrement by 1
* Char 2 - always Y
* Char 3 - increment by 1

This pseudocode can return the proper label value
```
var seed = (73-Quality)*2;
char[]Label = new char[4];
for (int c = 0; c<4; c++)
  {  
    char NewChar;  
    if ((c==0) || (c==2))
    {
       NewChar = (seed % 26) + 65;      
    }
    else
    {//c==1 or c==3
      NewChar = (seed % 10) + 48;
    }
    label[c] = NewChar;
    seed = seed + quality + 30
  }
  return label.ToString();
```

### Traps & Triggers

A trap is a special object that performs an operation on the game world when triggered. Triggers are special objects that are linked to a regular object or exist within the game world that when activated initiate the action of a trap. The trigger can contain paramters for the operation of the trap.

Traps and Triggers are linked to each other and can be linked in a change of actions that allow for complex events.

Example. A swich is connected to a use trigger which is connected to a door trap. When the swithch is pressed the use trigger fires and activates the door trap which will tell a specified door to open.

#### Traps
##### a_arrow trap
An arrow trap is used to fire projectiles. The item type created is controlled by the trap ``quality`` and ``owner`` values.	
``Item Type ID`` = (``quality`` << 5) | ``owner`` set in 

The launch vector for the "arrow" is simply the heading of the trap.

##### a_bridge trap
Toggles the spawning and despawning of a row of bridges of length given by the trap  ``quality``.

The row starts at trigger ``X`` and ``Y`` tile.

The trap ``heading`` controls the direction the bridges spawn (cardinal directions only) 0=north 2= east 4 = south and 6=west

Trap ``zpos`` controls the height where the bridges spawn.

Trap ``Owner`` is used to control the texture of the bridge floor

If the msb bit is set on ``owner`` then the trap will remove the bridges at the targeted location.

##### a_change from trap
Use to change a rectangle of tiles in a range starting at bottom left at the location of the change_from trap and ending at top right at a position given by a linked ``change_to_trap``. 

The tiles in the range must match with specified criteria defined in this trap and the changes to be made are defined on the ``change_to_trap`` 

A formula involving ``Heading`` and ``zpos`` seems to define a  floor texture to match for changing. TO CONFIRM
``(heading | (((zpos >> 4) & 0x1) << 3));``

##### a_change to trap
Used with the ``change_from`` trap to change a range of tiles.

The ``quality`` value sets the ``wall texture``.

The ``owner`` value sets the ``tile type``. Either ``open`` or ``solid``.

The ``zpos`` value sets the ``floor height``.

The ``floor texture`` is set by the formula ``(heading | (((zpos >> 4) & 0x1) << 3))`` TO RECONFIRM.

##### a_change terrain trap
Changes a tile from one type to another. It works over a range of tiles that are set by the traps ``X`` and ``Y`` values starting at the trigger ``X`` and ``Y``.

``Floor Texture`` is set by ``(quality >> 1) & 0xf``

``Tile Type`` is given by ``(quality & 0x01)``

The trap ``zpos`` will set the height of the ``open`` tile except when it's value is 120. In that case the trigger ``zpos`` is used instead.

In ``UW2`` the ``wall texture`` can be set by the ``owner`` value when it is less than 63d.

##### a_check variable trap
Checks a variable numbered ``zpos``. 

When the comparison is true the trigger references by the ``link`` field will fire.

In ``UW2``, if the comparison is false then any trigger referenced in the ``next`` value will fire.

``Heading`` gives the value to compare with.

In ``UW1`` there is only one array of game variables. 

In ``UW2`` there are four known variable arrays and the array to use is given by the ``heading`` value. The possble values are:

  3 X-CLOCK
  4 Game Variables
  5 A bitfield list
  6 Quest Flags

TODO: Provide more info on the variable lists in their own section.

##### a_combination trap
TODO: Find this out. ``UW1`` only??

##### a_create object trap
Creates a new object using the object referenced by the ``link`` field as a template. 

TODO: This trap has a random chance of running when sleeping to spawn monsters. Reconfirm the behaviour here.

##### a_damage trap
TODO: Reconfirm. 


##### a_delete object trap
Removes the object pointed to in the ``link`` field from the world.
As the ``link`` is deleted then all trap/trigger execution halts at this trap.

##### a_do trap or a_hack_trap
The ``do`` and ``hack`` traps are special types of trap the perform advance functions. ``Do`` is the term for ``UW1`` and ``hack`` for ``UW2``.
The ``quality`` value defines what the trap is.

###### Camera Trap
``Quality`` 2

Moves the game camera to the location and points it in the direction of the trap.

###### Platform Trap
``Quality`` 3

###### Trespass Trap
``Quality`` 5

###### Class Object Trap
``Quality`` 10

Spawns class specific objects to the player in ``UW2``. Used in the hidden room in the Avatar quarters in ``Brittania``.

###### Fraznium Forcefield
``Quality`` 11

A force field that allows passage when fraznium gloves or crown are worn

###### Unused Oscillating Trap
``Quality`` 12

Appears to oscillate a row of tiles. Trap ``owner`` value increments on each call.

###### Colour Cycling Trap
``Quality`` 14

Cycles wall and floor colours.

``Owner`` From value of textures
``Zpos`` To value of textures.

The range of tiles is along the game x axis for ``ypos`` number of tiles.

###### Ice Floor Collapse Trap
``Quality`` 17

Collapses the ice floor tiles in the ``Ice Caverns``. An acrobat check is performed before the ice will break

The skill check is based on the ``weight`` carried by the player. If ``weight/12`` is 20 or less then the check value is 0. Otherwise the check will be ``weight/12`` vs ``Acrobat`` skill.

The new texture for the floor after collapsing is set to ``xpos | (ypos<<3)``

The new floor height will be the original height minus 1.

* The trap is based on a regular timer trigger, not on player motion over the tile.

###### Switch Puzzle Reset Trap
``Quality`` 18

Resets the switch puzzle on Scintillus Level 5.

###### Platform Puzzle Reset Trap
``Quality`` 19

Resets the platform puzzle on Scintillus Level 7

###### Rising Platforms Trap
``Quality`` 20

Use for the rising platforms on Level 42 (Scintillus)

###### Loth Tomb Switches
``Quality`` 21 and 22

Used for the moving switches in ``Loth's Tomb``

* ``Quality`` 22 is an unused variant where it sets ``owner`` to 1.
  
###### TMAP Change Trap
``Quality`` 23

Changes the texture of a texture map object. See trap with ``quality`` 28 below

###### Bullfrog Trap
``Quality`` 24

TODO: Document the bullfrog.
* ``UW1`` only
  
###### Change Graffiti Trap
``Quality`` 24

Changes graffiti in the ``Pits Of Carnage``

###### Bly Skup Chamber Trap
``Quality`` 25

Evaluates the conditions for spawning a new Bly Skup Ductosnore.

###### Scintillus Force Field Trap
``Quality`` 26

Used for the force field on Scintillus level 5
TO CONFIRM: This is the up/down forcefield??

###### Change Object Quality Trap
``Quality`` 27

Changes the ``quality`` of the ``link`` object to the trap ``owner`` value.

###### Change TMAP Trap
``Quality`` 28
Change a tmap object to use a different texture.
Trap will change the ``owner`` value of the tmap.
* This is possible used for more than changing tmaps as it will change any linked object ``owner``.

###### Random Button Flicking Trap
``Quality`` 29

This trap randomly flicks traps. Used in ``Talorus`` level 1.

###### Avatar is a Coward Trap
``Quality`` 30

If the avatar flees combat in the pits this trap will update the game state to end the arena duel and change the win/loss records.

See the section on the ``Pits Of Carnage`` for details on how the arena works.

###### Arena of Fire Safety Trap
``Quality`` 31

This trap will fire on a trigger in the arena and detect if any NPC combatants are standing in lava. If so they are teleported to safety.

###### QBert Puzzle Trap.
``Quality`` 32

See the section on Qbert for more details.

###### Bottle Recycler Trap
``Quality`` 33

Use to recycle glass bottles on a target tile and spawn the ``monetary`` value in gold coins.

###### The Castle Goes Dry Trap
``Quality`` 34

Changes various environmental details in the castle after arriving in the ``Ice Caverns``

Eg stops the fountains, does things with mushrooms etc.

###### Light Sphere Recharge Trap
``Quality`` 35

Sets the ``quality`` of the light sphere placed in a target location to 64.

###### Britannia NPC Teleport
``Quality`` 36

Triggered after talking to Lord British. Moves NPCs to different locations in the castle.
TODO Reconfirm.

###### Unknown Trap 37
``Quality`` 37

Not seen in the wild but appears to be related to the ``*SCD.ARK*`` file.

###### Spoil Healing Potion Trap
``Quality`` 38

Trap used in ``Loth's Tomb`` to find any healing potion in the player inventory and transform them into a poisoned potion.

###### Change Visibility Trap
``Quality`` 39

Used to change the visibility of an object.

###### Vending Machine Selection Trap
``Quality`` 40

Used to change the game variable that controls the currently selected vending machine item.

###### Vending Machine Spawning Trap
``Quality`` 41

Used to spawn the currently selected vending machine selection.

###### Vending Machine Sign Trap
``Quality`` 42

Used to set the vending machine sign with the current selection.

###### A Talking Door!
``Quality`` 42

Use to trigger the talking door conversation in ``UW1``.


###### Change NPC Goal Trap
``Quality`` 43

Used to change the goal for a specific type of NPC
Eg. When you pick up the map piece in ``Loth's Tomb`` 1 it will make all the skeletons attack the player.

###### Sleep Trap
``Quality`` 44

Used to go to sleep when using "bridge based" beds, bridges that have a straw bed texture made to look like beds.

###### Unknown Automap Trap
``Quality`` 45

Not observed yet. Seems to be related to updating ``automap`` data.

###### Start Conversation Trap
``Quality`` 50

Used in ``UW1`` to trigger a conversation with NPC number #251 in ``Tybal's Lair`` when the player gets trapped in the prison area.

###### Gem Face Rotate
``Quality`` 54

Rotates the gem face of the blackrock gem and updates the appropiate game variable that controls what world the gem will teleport to.

TODO: Add the variable number here.

###### World Teleport Trap
``Quality`` 55

Used to teleport from the blackrock gem to a hard-coded location in another world. Available worlds are in game variable TODO and the target world in game variable TODO.


###### Unknown AI Goal Trap 62
``Quality`` 62
Currently unknown purpose. Used in ``Britannia``, ``Prison Tower`` and ``Killorn`` for an unknown purpose.

The current working theory is that it is used to direct a NPC to take an action

EG in ``Britannia`` it appears to be linked to quest 109 and 112 which is set when the player is arrested for fighting in the castle. It will set Lord British's goal to 12 (based on the ``owner`` value) and causes British to walk to the prison cell to talk to the Avatar.

##### a_door trap
Opens or closes the door in the tile pointed to by the trigger ``X`` and ``Y``

The ``quality`` value gives the mode of operation:

|Mode | Action  |
|-----|---------|
| 0   | Lock    |  
| 1   | Open    |
| 2   | Close   |
| 3   | Toggle  |


##### a_flam rune
An in-world rune trap that explodes and causes damage to the player

TODO: Confirm mechanics here.

##### a_jump trap
Launches a character up in the air.

The ``quality`` of the trap controls the strength of the jump trap.

##### a_null trap
A trap that performs no actions. Used to link trap/trigger chains.

##### a_pit trap
A trap that forms or closes a deep pit in the ground.

``Quality`` or possibly first 4 bits defines the texture of the tile to create at the base of the pit.

``Owner`` does the same for the floor texture at the top of the pit when closed up.

``Zpos`` is the height of the floor


##### a_proximity trap
This trap behaves more like a trigger as it takes effect when the player enters a plane given by a range that is ``owner`` by ``quality`` tiles in size starting at the position of the trap.

The ``zpos`` gives the height of the range.


##### a_set variable trap
Sets the game variable that is defined by ...

TODO: This is a complicated one to explain. I'll swing around to it.

##### a_skill trap
Looks like this trap does a skill check when triggered.

``Quality`` appears to be the skill number to use.

``Owner`` appears to be the target skill value needed to suceed.

##### a_special effects trap
Performs a special effect in the game world.

``Quality`` controls what effect is played.
| ``Quality`` |  Effect      |
|-------------|--------------|
|      1      |Unknown       |
|      2      |Guardian Laugh|
|      3      |Unknown       |
|      4      |Earthquake*   |
|      5      |Red Flash     |
|      6      |Black Flash   |
|      7      |Orange Flash  |
|      8      |Black Flash   |

* Owner controls how long the earthquake lasts


##### a_spelltrap
Casts a spell given by the ``owner`` and ``quality`` values

Spell Number is ``((quality & 0xf) << 4) | (owner & 0xf)``

* Given that cutscenes are spells this is used in some places to play cutscences when a trigger is activated.

##### a_teleport trap
Teleports the player to another tile and/or level

``Quality`` gives destination tile X
``Owner`` gives destination tile Y
``zpos`` If 0 then destination is on the same level, if not 0 then ``zpos`` is the target level to go to.

* It is currently unknown how the arrival ``zpos`` coordinate is set when moving between levels.
 
##### a_text string trap
Displays a string of text in the message scroll. The text will always be from string block 9.

In ``UW1``, the string number is given by ``(64 * dungeon_level) + owner``

In ``UW2``, the string number is given by ``(32 * quality + owner)``

##### a_tym rune
An inworld trap rune that paralyses the player for a period.

TODO: Confirm paralyse time.

##### a_ward trap or a_tell trap
A special trap that is formed by the rune of warding spell.

When an NPC collides with the trap a text message will inform the player that a creature has collided with the trap at a relavitve position to the player.

A small amount of damage may also be applied to the create. TO CONFIRM 

##### an_experience trap
A trap that will increase or decrease the experience points for the player.
TODO: Exact math involved here.

##### an_inventory trap
A trap that will check the player inventory for a specific item
The ``item id`` to find is ``("quality" << 5) | owner``

##### an_oscillator trap
A trap that raises and lowers a row of tiles in an oscilating pattern.

Based on current understanding
``X`` is the current direction of oscillation
``owner`` is the max floor height to reach.
``Y`` or ``zpos``(likely) is possibly the min height for the oscillation 

#### Triggers
##### a_close trigger
A trigger that fires when a door is closed

##### a_look trigger
A trigger that fires when a look based action. Eg looking at a texture map occurs.

##### a_move trigger
A trigger that fires when the avatar is moving within a tile

##### a_pick up trigger
A trigger that fires when an object is picked up. The trigger will be the ``link`` object or part of a containers contents.

##### a_pressure release trigger
An in-world trigger that fires when enough weight is removed from a pressure plate to raise it up.

##### a_pressure trigger
An in-world trigger that fires when sufficent weight is added to a pressure plate to depress it.

##### a_scheduled trigger
A trigger that is evaluated on level entry as part of ``*SCD.ARK*`` processing.

##### a_step on trigger
Unknown but possibly this means the floor of a tile is being stepped on. 

##### a_timer trigger
A trigger that fires at regular intervals. Timing appears to be based on ``zpos`` seconds intervals. Timer triggers only process when the player is in the area of the trigger.

##### a_use trigger
A trigger that fires when an object (eg a switch) is used.

##### an_enter trigger
A trigger that fires when a player enters a tile.

##### an_exit trigger
A trigger that fires when a player exits a tile.

##### an_open trigger
A trigger that fires when a door is opened.

##### an_unlock trigger
A trigger that fires when a door is unlocked.


## Quests
### ``UW1`` Quests
| Quest No | Quest                                                  | Notes                                       |
|----------|--------------------------------------------------------|---------------------------------------------|
| 0        | Dr. Owl's assistant Murgo freed                        |                                             |
| 1        | talked to Hagbard                                      |                                             |
| 2        | Met Dr. Owl?                                           |                                             |
| 3        | permission to speak to king Ketchaval                  |                                             |
| 4        | Goldthirst's quest to kill the gazer (1: gazer killed) |                                             |
| 5        | Garamon, find talismans and throw into lava            |                                             |
| 6        | friend of Lizardman folk                               |                                             |
| 7        | ?? (conv #24, Murgo)                                   |                                             |
| 8        | book from Bronus for Morlock                           |                                             |
| 9        | "find Gurstang" quest                                  |                                             |
| 10       | where to find Zak, for Delanrey                        |                                             |
| 11       | Rodrick killed                                         |                                             |
| 32       | status of "Knight of the Crux" quest                   |                                             |
|          | Stage 0                                                | no knight                                   |
|          | Stage 1                                                | seek out Dorna Ironfist                     |
|          | Stage 2                                                | started quest to search the "writ of Lorne" |
|          | Stage 3                                                | found writ                                  |
|          | Stage 4                                                | door to armoury opened                      |
| 36       | No of talismans still to destroy.                      |                                             |
| 37       | Garamon dream stages                                   |                                             |




### ``UW2`` Quests

| Quest No                                    | Description                                                                                              |
|---------------------------------------------|----------------------------------------------------------------------------------------------------------|
| 0                                           |  ``Prison Tower`` related - The troll is released                                                                      |
| 1                                           |  ``Prison Tower`` related - Bishop is free?                                                                            |
| 2                                           |  ``Prison Tower`` related - Borne wants you to   kill bishop                                                           |
| 3                                           |  ``Prison Tower`` related - Bishop is dead                                                                             |
| 6                                           |  Helena asks you to speak to   praetor loth                                                              |
| 7                                           |  Loth is dead                                                                                            |
| 8                                           |   Kintara tells you about Javra                                                                          |
| 9                                           |   Lobar tells you about the   "virtues"                                                                  |
| 10                                          |  ``Prison Tower`` related                                                                                              |
| 11                                          |  Listener under the castle is dead.                                                                      |
| 12                                          |  used in ``Ice Caverns`` to say the   avatar can banish the guardians presence. Wand of altara?              |
| 13                                          |  Mystral wants you to spy on altara                                                                      |
| 14                                          |  Likely all lines of power have   been cut.                                                              |
| 15                                          |  Altara tells you about the   listener                                                                   |
| 18                                          |  You learn that the Trikili can   talk.                                                                  |
| 19                                          |  You know Relk has found the black   jewel (josie tells you)                                             |
| 20                                          |  You've met Mokpo                                                                                        |
| 22                                          |  Blog is now your friend(?)                                                                              |
| 23                                          |  You have used Blog to defeat   dorstag                                                                  |
| 24                                          |  You have won a duel in the arena                                                                        |
| 25                                          |  You have defeated Zaria in the   pits                                                                   |
| 26                                          |  You know about the magic scepter   (for the Zoranthus)                                                  |
| 27                                          |  You know about the sigil of   binding/got the djinn bottle(by bringing the scepter to zorantus)         |
| 28                                          |  Took Krilner as a slave                                                                                 |
| 29                                          |  You know Dorstag has the gem(?)                                                                         |
| 30                                          |  Dorstag refused your challenge(?)                                                                       |
| 32                                          |  Met a Talorid                                                                                           |
| 33                                          |  You have agreed to help the   talorid (historian)                                                       |
| 34                                          |  Met or heard of Eloemosynathor                                                                          |
| 35                                          |  The vortz are attacking!                                                                                |
| 36                                          |  Quest to clarify question for Data   Integrator                                                         |
| 37                                          |  ``Talorus`` related (checked by   futurian)                                                                 |
| 38                                          |  ``Talorus`` related *bliy scup is   regenerated                                                             |
| 39                                          |  ``Talorus`` related                                                                                         |
| 40                                          |  Dialogian has helped with data   integrator                                                             |
| 43                                          |  Patterson has gone postal                                                                               |
| 45                                          |  Janar has been met and befriended                                                                       |
| 47                                          |  You have recieve the quest from   the triliki                                                           |
| 48                                          |  You have dreamed about the void                                                                         |
| 49                                          |  Bishop tells you about the gem.                                                                         |
| 50                                          |  The keep is going to crash.                                                                             |
| 51                                          |  You have visited the ice caves   (``Brittania`` becomes icy)                                                |
| 52                                          |  Have you cut the line of power in   the ``Ice Caverns``                                                     |
| 54                                          |  Checked by Mors Gotha? related to   keep crashing                                                       |
| 55                                          |  Banner of ``Killorn`` returned (based   on *SCD.ARK* research)                                                |
| 58                                          |  Set when meeting bishop. Bishop   tells you about altara                                                |
| 60                                          |  Possible ``Prison Tower`` variable.   used in check trap on second highest level                            |
| 61                                          |  You've brought water to Josie                                                                           |
| 63                                          |  Blog has given you the gem                                                                              |
| 64                                          |  Is mors dead                                                                                            |
| 65                                          |  Pits related (checked by dorstag)                                                                       |
| 68                                          |  You have given the answers to   nystrul and the invasion (endgame) has begun.                           |
| 104                                         |  Set when you enter scintilus level   5 (set by variable trap)                                           |
| 105                                         |  Set when the air daemon is   absorbed. (see also xclock1 and xclock3 changes)                           |
| 106                                         |  Got or read mors spellbook                                                                              |
| 107                                         |  Set after freeing praetor loth and   you/others now know about the horn.                                |
| 109                                         |  Set to 1 after first LB   conversation. All castle occupants check this on first talk.                  |
| 110                                         |  Checked when talking to LB and   Dupre. The guardians forces are attacking                              |
| 112                                         |  checked when talking to LB. You   have been fighting with the others                                    |
| 114                                         |  checked when talking to LB. The   servants are restless                                                 |
| 115                                         |  checked when talking to LB. The   servants are on strike                                                |
| 116                                         |  The strike has been called off.                                                                         |
| 117                                         |  Mors has been defeated in ``Killorn``                                                                        |
| 118                                         |  The wisps tell you about the   trilikisssss2                                                            |
| 119                                         |  Fizzit the thief surrenders                                                                             |
| 120                                         |  checked by miranda?                                                                                     |
| 121                                         |  You have defeated Dorstag                                                                               |
| 122                                         |  You have killed the bly scup   ductosnore                                                               |
| 123                                         |  Relk is dead                                                                                            |
| 124 &   126  |          are referenced in teleport_trap                                                                                                |
| 128                                         |  0-128 bit field of where the lines   of power have been broken.                                         |
| 129                                         |  How many enemies killed in the   pits (also xclock 14)                                                  |
| 131                                         |  You are told that you are in the   ``Prison Tower`` =1                                                      |
| 132                                         |  Set to 2 during Kintara   conversation                                                                  |
| 133                                         |  How much Jospur owes you for   fighting in the pits                                                     |
| 134                                         |  The password for the ``Prison Tower``   (random value)                                                      |
| 135                                         |  Checked by goblin in sewers  (no of worms killed on level. At more than   8 they give you fish)         |
| 143                                         |  Set to 33 after first LB   conversation. Set to 3 during endgame (is this what triggers the cutscenes?) |


#### The X Clock
In ``UW2`` there are 15 special game variables called X Clocks. These are special incrementing variables that track progress  throughout the game.

The currently identified x clocks and their values are are 
```
1=Miranda conversations & related events in the castle
  1 - Nystrul is curious about exploration.Set after entering lvl 1 from the route downwards. (set variable traps 17 may be related)
  2 - After you visited another world.  (variable 17 is set to 16), dupre is tempted
  3 - servants getting restless
  4 - concerned about water, dupre is annoyed by patterson
  5 - Dupre is bored / dupre is fetching water
  6 - UNKNOWN
  7 - Miranda wants to talk to you pre tori murder
  8 - tori is murdered
  9 - Charles finds a key
  11 - Go see Nelson (before he is murdered by Patterson)
  12 - Patterson kills Nelson
  13 - Patterson is dead
  14 - Gem is weak/Mors is in ``Killorn``(?)
  15 - Nystrul wants to see you again re endgame
  16 - Nystrul questions have been answered Mars Gotha comes
2=Nystrul conversations and no of blackrock gems treated
3=Djinn Capture
  2 = balisk oil is in the mud
  3 = player bathed in oily mud
  4 = baked in lava
  5 = iron flesh cast (does not need to be still on when you break the bottle)
  6 = djinn captured in body
14=Tracks number of enemies killed in the ``Pits Of Carnage``
15=Used in multiple convos. Possibly tells the game to process a change when updated??

```

## Game worlds and Levels
### ``UW1`` Levels

#### ``Tybal's Lair``
TODO: Why no magic

#### The ``Ethereal Void`` Endgame Map

### ``UW2`` Levels
#### ``Brittania``

#### ``Pits Of Carnage``
TODO: Write up how the arena works.

#### The ``Ethereal Void``

##### QBert Puzzle.
TODO Document this puzzle

## NPCS
### NPC Basics

### AI Goals

### ``UW2`` Castle Schedule

## Strings
### Decoding

### String Blocks

## Conversations
### Conversation Machine Code Specification

### Imported Functions

### Conversation Variables

## Unanswered Questions and Problems


## Code Examples


## Reverse Engineering