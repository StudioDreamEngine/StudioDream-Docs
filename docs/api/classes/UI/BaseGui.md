---
title: BaseGui
description:
icon: studiodream/Unknown
---

# :studiodream-Unknown: BaseGui

{{ inherits("Thing") }}

This is the base class for all GUI Things

{{ abstract() }}

{{ notnewable() }}


## Properties

### AbsolutePosition:Vector2 { property }
``Accessible`` ``Internal``

The position of the thing relative to the viewport

### AbsoluteSize:Vector2 { property }
``Accessible`` ``Internal``

The size of the thing relative to the viewport


## Methods

### GetOffsetPosition():Vector2 { method }
``Accessible``

Get the absolute position relative to the parent thing

### GetAbsolutePosition():Vector2 { method }
``Accessible``

Missing Documentation!

### GetDisplayPosition():Vector2 { method }
``Accessible``

Get the true position where the thing is displayed (On the screen)

### GetAbsoluteSize():Vector2 { method }
``Accessible``

Missing Documentation!

### Draw():void { method }
``Accessible``

Missing Documentation!

