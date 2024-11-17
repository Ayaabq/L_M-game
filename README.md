# Logic Magnets Game - README

This project is a grid-based game named Logic Magnets, developed as part of my coursework in the Search Algorithms subject at ITE-DU.

## Overview

The game involves moving pieces on a grid with specific logic and behavior for each piece, aiming to achieve designated target positions with the fewest moves. The main components of this game include a search algorithm implemented using BFS,DFS, and other search algorithmes to find the optimal solution, as well as a Pygame-based graphical interface will added in the future.

## Features

Grid-based Gameplay: Players can move pieces on a grid according to specific rules and interactions.

Piece Interactions: Includes unique behaviors for pieces, such as attraction and repulsion.

Search Algorithm Solver

## Requirements
Python 3.x

## About

This project is submitted as a homework assignment for the Search Algorithm subject.

Student Name: ايه مأمون بقله

Class: 3



## Acknowledgments


Thanks to  MS Sally Youssef and ITE-DU for the guidance provided in this assignment.

---



## توصيف المسألة كخوارزمية بحث:

## **1- فضاء الحالات (State Space)**
فضاء الحالات في هذه اللعبة هو كل الترتيبات الممكنة للقطع على رقعة اللعب التي تتكون من شبكة `n×n`.  
### **تمثيل الحالة**  
تتضمن الحالة:
- **موقع القطع المغناطيسية والحديدية**:
  - القطع **البنفسجية** التي تقوم بدفع القطع في نفس السطر أو العمود.
  - القطع **الحمراء** التي تجذب القطع في نفس السطر أو العمود.
  - القطع **الرمادية** التي لا تتحرك إلا تحت تأثير المغناطيسات.
- **الخانات الفارغة**: الأماكن التي يمكن تحريك القطع المغناطيسية إليها.  
- **خانات الهدف**: الخانات التي يجب تغطيتها لتحقيق الفوز.  

### **محتويات الحالة**  
- يتم تمثيل الرقعة باستخدام مصفوفة ثنائية الأبعاد تحتوي على:
  - نوع الخلية (فارغة، قطعة حديدية، مغناطيسية، هدف).
  - موقع كل قطعة (إحداثيات الخلايا `x, y`).

---

## **2- الحالة الابتدائية (Initial State)**
### **تحديد المواقع الأولية**
- عند بداية اللعبة، يتم تحديد مواقع جميع القطع بشكل مسبق وفقًا للمستوى المختار من قبل اللاعب.  

### **محتويات الحالة الابتدائية**
- القطع المغناطيسية (الحمراء والبنفسجية) موضوعة في أماكنها.
- القطع الحديدية الرمادية موزعة بشكل يناسب التحدي.
- الخانات الفارغة التي تمثل أماكن ممكنة للتحريك.
- خانات الهدف التي يجب ملؤها.

---

## **3- العمليات (Actions)**
### **التحريك** 
- يمكن تحريك القطع المغناطيسية (الحمراء والبنفسجية) فقط إلى الخانات الفارغة.  
- عند تحريك قطعة مغناطيسية، تتفاعل القطع الأخرى بناءً على قواعد اللعبة:
  - **القطع البنفسجية**:
    - تقوم **بدفع** جميع القطع المتصلة بها (في نفس الصف أو العمود) بعيدًا عنها، بشرط عدم وجود عوائق.
    - إذا كانت أي قطعة في الخط المتصل محجوبة، فلن تتحرك أي قطعة في هذا الاتجاه.
  - **القطع الحمراء**:
    - تقوم **بسحب** جميع القطع في نفس الصف أو العمود باتجاهها، بشرط أن تكون المسافة بين القطع فارغة.

### **القيود**
- لا يمكن تحريك القطع الرمادية مباشرة، لكنها تتأثر بالمغناطيسات.
- لا يمكن تجاوز القطع الأخرى أو الخروج عن حدود الرقعة.

### **الوظائف الخاصة بالتحريك**
1. يتم التأكد من إمكانية تحريك القطعة باستخدام دالة `can_move_piece`.
2. عند تنفيذ الحركة، يتم تحديث الرقعة باستخدام دوال خاصة مثل:
   - `move_adjacent_pieces_away` للتنافر.
   - `move_adjacent_pieces_towards` للتجاذب.

---

## **4- الحالات النهائية (Goal States)**
- الحالة النهائية هي عندما يتم تحقيق الشروط التالية:
  1. تغطية جميع خانات الهدف بقطع (مغناطيسية أو حديدية).
  2. أن تكون الخانات المغطاة متوافقة مع قواعد اللعبة.
  3. يتم فحص حالة الفوز باستخدام دالة `all_targets_filled` التي تتحقق مما إذا كانت كل خانات الهدف مشغولة بشكل صحيح.

---

## **5- آلية الحل (Search Algorithms)**
تم تصميم اللعبة لتدعم استخدام خوارزميات بحث ذكية مثل:
- **BFS (بحث أولاً بالعرض)**: يتم استخدامه لتوليد جميع الحالات الممكنة والتحقق من المسار الأقصر للوصول إلى الهدف.
- **DFS (بحث أولاً بالعمق)**: يتم استخدامه لاستكشاف الحلول بشكل متعمق ولكنه قد يكون أقل كفاءة في بعض الحالات.

### **آلية العمل**
1. تبدأ الخوارزمية بالحالة الابتدائية.
2. يتم توليد الحالات الجديدة باستخدام الدالة `generate_all_possible_moves`، التي تأخذ الحالة الحالية وتُرجع كل الحالات الممكنة بناءً على الحركات المتاحة.
3. يتم فحص كل حالة للتأكد مما إذا كانت حالة فوز.
4. عند العثور على الحالة النهائية، يتم استخراج المسار عن طريق تخزينه في كل مرة 

---


<<<<<<< HEAD
Thanks to MS Sally Youssef and ITE-DU for the guidance provided in this assignment.

=======
>>>>>>> 3abda7a3c8422f4d286b564a041e5675cadfec53
