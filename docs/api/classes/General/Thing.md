---
title: Thing
description:
icon: studiodream/Unknown
---

# Thing

{{ inherits("ClassicObject") }}

{{ inherited_by(["BaseGui"]) }}

This is the base class for all objects

{{ abstract() }}

{{ notnewable() }}


## Properties

### Serializable:boolean { property }
``Internal``

Missing documentation!

### Parent:Thing { property }
``Accessible`` ``Serialized``

Missing documentation!

### Name:string { property }
``Accessible`` ``Serialized``

Missing documentation!

### Type:string { property }
``Accessible``

Missing documentation!

### UUID:string { property }
``Accessible`` ``Internal``

Missing documentation!


## Methods

### BindConstraint():void { method }
``Accessible`` ``Internal``

Missing documentation!

### SetConstraint():void { method }
``Accessible`` ``Internal``

Missing documentation!

### UnbindConstraints():void { method }
``Accessible`` ``Internal``

Missing documentation!

### FindConstraintOfType():void { method }
``Accessible`` ``Internal``

Missing documentation!

### GetProperty():void { method }
``Accessible`` ``Internal``

Missing documentation!

### FindFirstAncestorWithClass(Class;string):Thing { method }
``Accessible``

Goes up in the tree until it finds a Object that matches the specified class

### Is():boolean { method }
``Accessible``

Checks if this object

### GetParentCallback():void { method }
``Accessible`` ``Internal``

Missing documentation!

### SetParent():void { method }
``Accessible`` ``Internal``

Missing documentation!

### DescendantOf():boolean { method }
``Accessible``

Missing documentation!

### IsA():boolean { method }
``Accessible``

Missing documentation!

### GetChildren():{ Thing } { method }
``Accessible``

Missing documentation!

### GetDescendants():void { method }
``Accessible``

Missing documentation!

### FindFirstChild():void { method }
``Accessible``

Missing documentation!

### ClearAllChildren():void { method }
``Accessible``

Missing documentation!

