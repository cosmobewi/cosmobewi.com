.. _dilution_lambda_paper:

===================================================
De la dilution des champs sans masse à l’énergie du vide
===================================================

Résumé
======

Nous proposons une interprétation phénoménologique simple de la
constante cosmologique : elle peut être vue comme l’**accumulation
d’énergie résiduelle** issue de la dilution des champs sans masse
(photons, neutrinos relativistes) lors de l’expansion de l’Univers.

En postulant qu’une fraction du travail thermodynamique
:math:`p\,dV` effectué par le rayonnement est stockée dans un réservoir
« vide », on retrouve une valeur compatible avec
:math:`\Omega_{\Lambda 0}\simeq 0.7` aujourd’hui — **sans invoquer
directement la QFT**.

---

1. Loi de dilution énergétique
==============================

La conservation de l’énergie-moment en espace-temps FLRW donne :

.. math::

   \dot{\rho} + 3H(1+w)\rho = 0,

avec :math:`w=p/\rho`.

Trois cas particuliers :

- **Champs sans masse** : :math:`w=1/3` → :math:`\rho\propto a^{-4}`
- **Matière massive** : :math:`w=0` → :math:`\rho\propto a^{-3}`
- **Vide** : :math:`w=-1` → :math:`\rho=\text{constante}`

Cette hiérarchie explique la cascade cosmologique :

.. code-block:: text

   Rayonnement  →  Matière  →  Vide

---

2. Hypothèse « conversion pdV → Λ »
===================================

Dans un volume comobile :math:`V\propto a^3`, le rayonnement vérifie :

.. math::

   dU_\gamma + p_\gamma dV = 0,
   \qquad p_\gamma = \tfrac{1}{3}\rho_\gamma,
   \qquad \rho_\gamma \propto a^{-4}.

**Postulat :** une fraction :math:`\eta` du travail
:math:`p_\gamma dV` cumulé des champs sans masse depuis un certain
redshift :math:`z_\star` est stockée en énergie du vide.

Alors, aujourd’hui :

.. math::

   \rho_{\Lambda 0} \simeq \eta \,\rho_{r0}\,z_\star,

soit, en densités réduites :

.. math::

   \Omega_{\Lambda 0} \simeq \eta \,\Omega_{r0}\,z_\star.

---

3. Ordres de grandeur
=====================

La densité de rayonnement aujourd’hui est :

.. math::

   \Omega_{r0} = \Omega_{\gamma 0}\,[1+0.2271\,N_{\rm eff}],
   \qquad \Omega_{\gamma 0} \simeq \tfrac{2.469\times10^{-5}}{h^2}.

Avec :math:`h=0.68` et :math:`N_{\rm eff}=3.044` :

.. math::

   \Omega_{r0} \simeq 9.03\times 10^{-5}.

Cas 1 — recombinaison (:math:`z_\star\approx 1100`) :

.. math::

   \eta \approx \tfrac{0.69}{0.099} \approx 6.95.

Cas 2 — égalité matière/rayonnement (:math:`z_\star\approx 3400`) :

.. math::

   \eta \approx \tfrac{0.69}{0.307} \approx 2.25.

👉 Avec :math:`\eta` d’ordre unité–quelques, on retrouve
:math:`\Omega_{\Lambda 0}\sim 0.7`.

---

4. Consistance dynamique
========================

Un couplage simple assure la conservation totale :

.. math::

   \dot\rho_r + 4H\rho_r = -Q, \\
   \dot\rho_m + 3H\rho_m = 0, \\
   \dot\rho_\Lambda = +Q,

avec :math:`Q = \eta(a)\,H\,\rho_r`.

En choisissant :math:`\eta(a)\propto a^3` (pondération par le volume),
on retrouve exactement la loi
:math:`\Omega_{\Lambda 0} \simeq \eta_0 \Omega_{r0} z_\star`.

Le paramètre effectif :math:`w_\Lambda^{\rm eff} = -1 - Q/(3H\rho_\Lambda)`
s’écarte de -1 de l’ordre :math:`10^{-4}` aujourd’hui — indétectable
actuellement.

---

5. Questions et défis
=====================

1. **Origine physique de :math:`\eta`**  
   Pourquoi une fraction du travail :math:`p\,dV` serait-elle convertie
   en énergie du vide ? Un mécanisme explicite reste à construire
   (couplage non minimal, running vacuum, viscosité, anomalies…).

2. **Choix de :math:`z_\star`**  
   L’égalité matière/rayonnement est un seuil naturel (activation par
   courbure :math:`R\neq 0`). La recombinaison est plus arbitraire. Une
   dépendance continue :math:`\eta(a)` semble plus réaliste.

3. **Conservation de l’énergie**  
   Une évolution de :math:`\rho_\Lambda` implique un transfert
   explicite. La cohérence avec les observations (SN Ia, âge de
   l’Univers, BBN) doit être vérifiée.

4. **Lien avec les autres composantes**  
   La matière noire n’a pas de pression (:math:`p\simeq 0`) → pas de
   source :math:`p\,dV`. Cette asymétrie doit être justifiée
   micro-physiquement.

5. **Stabilité et données**  
   Le modèle correspond-il à une énergie sombre dynamique (quintessence)
   ou à un « vide » réellement constant ? Les contraintes actuelles
   tolèrent \(|w+1|\lesssim 10^{-2}\), mais les futurs relevés
   (DESI, Euclid, LSST) pourraient détecter des écarts à
   :math:`10^{-3}`.

---

6. Signatures distinctives
==========================

- **Corrélation prédite** entre :math:`\Omega_{\Lambda 0}` et
  :math:`\Omega_{r0}` (donc :math:`N_{\rm eff}`).
- **Déviation phantom locale** de :math:`w_\Lambda^{\rm eff}(z)` autour
  de :math:`z_\star`.
- **Transition tardive douce** dans :math:`H(z)` testable par
  chronomètres cosmiques et BAO radiales.
- **Effet ISW** possible si activation proche du découplage.

---

Conclusion
==========

Nous avons proposé un mécanisme simple où la constante cosmologique
émerge de la **conversion partielle du travail des champs sans masse en
énergie de vide**.

Ce scénario reproduit :math:`\Omega_{\Lambda 0}\sim 0.7` avec un
paramètre d’efficacité :math:`\eta \sim 2{-}7`, **sans recourir à la
QFT**. Il prédit des signatures distinctives, notamment :

- une **corrélation** entre :math:`\Omega_{\Lambda 0}` et
  :math:`N_{\rm eff}`, testable avec les données actuelles,
- une **déviation locale** de :math:`w_\Lambda^{\rm eff}(z)`, accessible
  aux futurs relevés (Euclid, LSST).

Bien que des développements microphysiques et des tests observationnels
précis restent nécessaires, cette approche offre une **alternative
phénoménologique viable** à l’interprétation standard de :math:`\Lambda`,
en la reliant naturellement à la **hiérarchie de dilution énergétique**
de l’Univers.
