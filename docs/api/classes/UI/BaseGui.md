---
title: BaseGui
description:
icon: studiodream/Unknown
---

# BaseGui

{{ inherits("Thing") }}

This is the base class for all GUI Objects

{{ abstract() }}

{{ notnewable() }}


## Properties

### AbsolutePosition:Vector2 { property }
``Accessible`` ``Internal``

The position of the object relative to the viewport

### AbsoluteSize:Vector2 { property }
``Accessible`` ``Internal``

The size of the object relative to the viewport


## Methods

### GetOffsetPosition():Vector2 { method }
``Accessible``

Get the absolute position relative to the parent object

### GetAbsolutePosition():Vector2 { method }
``Accessible``

Missing documentation!

### GetDisplayPosition():Vector2 { method }
``Accessible``

Get the true position where the object is displayed (On the screen)

