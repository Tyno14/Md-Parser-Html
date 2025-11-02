---
title: "Md-Parser-Html"
description: "Parseur Python : convertit des fichiers .md en pages HTML statiques, responsives et stylisées."
date: "2025-05-14"
tags: ["python","markdown","html","parser","cli"]
lang: "fr"

# Configuration techStack
techStack:
  - name: "Python"
    category: "language"
    icon: "🐍"
  - name: "Regex (module re)"
    category: "tool"
    icon: "⚙️"
  - name: "Argparse"
    category: "tool"
    icon: "⌨️"
  - name: "HTML5"
    category: "language"
    icon: "🌐"
  - name: "CSS3"
    category: "language"
    icon: "🎨"

# Architecture du projet
architecture:
  overview: "L'architecture est celle d'un processeur de flux de texte (stream processor) en ligne de commande. Le script principal (main.py) utilise argparse pour gérer les entrées (fichiers ou dossiers). Le cœur logique, mdparser.py, lit le fichier .md ligne par ligne et applique une série d'expressions régulières (Regex) pour transformer 'à la volée' la syntaxe Markdown en balises HTML. Le résultat est ensuite encapsulé dans un template HTML/CSS prédéfini pour produire le fichier final."
  components:
    - "main.py (Gestionnaire CLI) : Point d'entrée qui utilise argparse pour interpréter les arguments de la ligne de commande (fichier d'entrée, dossier, option --output)."
    - "mdparser.py (Moteur de Parsing) : Le cœur du projet. Contient la logique de conversion ligne par ligne et les expressions régulières (Regex) qui identifient et remplacent la syntaxe Markdown."
    - "convert_line (Fonction principale) : La fonction centrale dans mdparser.py qui applique séquentiellement toutes les règles Regex à une seule ligne de texte."
    - "generate_html (Assembleur final) : Fonction qui prend le contenu HTML converti et l'insère dans un template HTML prédéfini (avec CSS)."
    - "Template HTML/CSS (Statique) : Une chaîne de caractères Python contenant la structure HTML et le CSS (responsive, mode sombre) qui encapsule le contenu converti."

# Diagrammes d'architecture (optionnel)
diagrams:
  - path: "https://raw.githubusercontent.com/Tyno14/Md-Parser-Html/main/.portfolio/diagrams/md-parser-architecture.svg"
    title: "Flux de parsing (Markdown vers HTML)"
    description: "Vue d'ensemble de l'architecture CLI et du moteur de parsing Regex"

# URLs et liens
demo_url: ""
demo_label: ""
github_url: "https://github.com/Tyno14/Md-Parser-Html"
---

## 🎯 Vue d'ensemble

<div class="overview-hero dark:bg-gradient-to-br dark:from-accent/10 dark:to-purple-900/10 bg-gradient-to-br from-indigo-50 to-purple-50 border dark:border-accent/20 border-indigo-200 rounded-2xl p-8 my-8 shadow-lg">
  <p class="text-lg dark:text-white/90 text-slate-700 leading-relaxed mb-6">
    Md-Parser-Html est un outil <strong>léger</strong> et <strong>puissant</strong> qui transforme vos fichiers Markdown bruts en pages HTML complètes. Écrit en <strong>Python pur</strong> sans dépendances, il gère la conversion de fichiers uniques ou de dossiers entiers. Le résultat est une page <strong>responsive</strong> et <strong>automatiquement stylisée</strong> (avec mode sombre), prête à être publiée, le tout via une simple ligne de commande.
  </p>
  
  <div class="stats-row grid grid-cols-2 md:grid-cols-4 gap-4 mt-6">
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">13</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Syntaxes Markdown gérées</div>
    </div>
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">0</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Dépendance externe</div>
    </div>
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">2</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Modes (Fichier / Dossier)</div>
    </div>
    <div class="stat-item text-center">
      <div class="stat-value text-3xl font-bold dark:text-accent text-indigo-600">1</div>
      <div class="stat-label text-sm dark:text-white/60 text-slate-600">Fichier CSS responsive (intégré)</div>
    </div>
  </div>
</div>

### Objectifs du projet

<div class="objectives-grid grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 my-8">
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🎓
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Valider le TP de l'ESGI
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Répondre aux exigences pédagogiques du TP "Markdown → HTML" de 3ème année, en démontrant la maîtrise du parsing de texte.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      ⚙️
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Maîtriser les Expressions Régulières
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Implémenter le cœur du parseur en utilisant exclusivement le module `re` de Python pour identifier et transformer les 13 syntaxes Markdown.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      ⌨️
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Créer un Outil CLI Fonctionnel
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Utiliser `argparse` pour offrir une interface en ligne de commande robuste, capable de gérer des fichiers ou des dossiers.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🎨
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Produire un HTML "Prêt à l'emploi"
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Encapsuler le contenu converti dans un template HTML5 valide, incluant un CSS responsive et un mode sombre.
    </p>
  </div>
  <div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 hover:scale-105 transition-all duration-300 hover:shadow-xl">
    <div class="icon-wrapper text-4xl mb-4 flex items-center justify-center w-16 h-16 rounded-full dark:bg-white/10 bg-slate-100 mx-auto">
      🐍
    </div>
    <h3 class="text-lg font-semibold mb-2 dark:text-white text-slate-900 text-center">
      Relever le défi "Python Pur"
    </h3>
    <p class="text-sm dark:text-white/70 text-slate-600 text-center leading-relaxed">
      Réaliser l'ensemble du projet en utilisant uniquement les bibliothèques natives de Python (`re`, `argparse`, `os`), sans dépendances tierces.
    </p>
  </div>
</div>

## ⚙️ Moteur de Parsing (Regex)

<div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 my-8">
  <p class="text-sm dark:text-white/70 text-slate-600 leading-relaxed mb-4">
    Le cœur du script repose sur une série d'<strong>expressions régulières (Regex)</strong> appliquées séquentiellement. Le module <code>re</code> de Python est utilisé pour identifier 13 syntaxes Markdown distinctes, des titres (<code>#</code>) aux images (<code>![]()</code>), et les remplacer "à la volée" par leurs balises HTML correspondantes.
  </p>
  <ul class="list-disc list-outside space-y-2 pl-5 text-sm dark:text-white/70 text-slate-600">
    <li><strong>Fonction <code>convert_line</code> :</strong> La fonction centrale qui orchestre l'application des règles Regex. L'ordre d'application est crucial (par exemple, traiter le <strong>gras</strong> avant l'<strong>italique</strong>).</li>
    <li><strong>Titres (H1-H3) :</strong> Utilise <code>re.sub(r'^### (.*)', '<h3>\\1</h3>', line)</code> pour remplacer les <code>#</code> en début de ligne.</li>
    <li><strong>Listes (ul/li) :</strong> Une règle simple remplace les <code>* </code> ou <code>- </code> par des balises <code><li></code>. Le script encapsule ensuite les blocs <code><li></code> consécutifs dans des balises <code><ul></code>.</li>
    <li><strong>Liens & Images :</strong> Les Regex les plus complexes qui utilisent des groupes de capture pour extraire à la fois le texte (<code>[]</code>) et l'URL (<code>()</code>).</li>
    <li><strong>Blocs de code :</strong> Détecte les <code>```</code> pour ouvrir et fermer les balises <code><pre><code>...</code></pre></code>, en gérant un état <code>in_code_block</code>.</li>
  </ul>
</div>

## ⌨️ Interface en Ligne de Commande (CLI)

<div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 my-8">
  <p class="text-sm dark:text-white/70 text-slate-600 leading-relaxed mb-4">
    Pour transformer le script en un outil réutilisable, l'interface en ligne de commande est gérée par le module natif <strong><code>argparse</code></strong>. Il fournit une expérience utilisateur claire avec des arguments définis, des messages d'aide (<code>-h</code>) et une validation des entrées.
  </p>
  <ul class="list-disc list-outside space-y-2 pl-5 text-sm dark:text-white/70 text-slate-600">
    <li><strong>Argument <code>--input</code> / <code>-i</code> :</strong> L'argument principal (requis) qui accepte le chemin vers un fichier <code>.md</code> ou un dossier.</li>
    <li><strong>Argument <code>--output</code> / <code>-o</code> :</strong> Un argument optionnel pour spécifier un dossier de sortie. S'il est omis, le script crée un dossier <code>html_output</code> par défaut.</li>
    <li><strong>Argument <code>--lang</code> / <code>-l</code> :</strong> Un argument optionnel pour définir la langue (<code>lang="fr"</code>) de la balise HTML, améliorant l'accessibilité.</li>
    <li><strong>Validation des chemins :</strong> Le script vérifie si le chemin d'entrée (<code>--input</code>) existe et s'il s'agit bien d'un fichier ou d'un dossier.</li>
  </ul>
</div>

## 📂 Traitement par Lot (Fichier vs Dossier)

<div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 my-8">
  <p class="text-sm dark:text-white/70 text-slate-600 leading-relaxed mb-4">
    Le script adapte intelligemment son comportement en fonction de l'entrée (<code>--input</code>). Il utilise le module <strong><code>os.path</code></strong> pour détecter s'il s'agit d'un fichier unique ou d'un dossier, lui permettant de fonctionner aussi bien pour une conversion simple que pour la génération d'un site statique.
  </p>
  <ul class="list-disc list-outside space-y-2 pl-5 text-sm dark:text-white/70 text-slate-600">
    <li><strong>Détection de mode :</strong> Utilisation de <code>os.path.isfile()</code> et <code>os.path.isdir()</code> sur l'argument d'entrée.</li>
    <li><strong>Mode Fichier :</strong> Si l'entrée est un fichier, le script exécute une conversion unique.</li>
    <li><strong>Mode Dossier (Batch) :</strong> Si l'entrée est un dossier, le script active une boucle récursive en utilisant <strong><code>os.walk()</code></strong>.</li>
    <li><strong>Préservation de l'arborescence :</strong> Le script maintient la structure des sous-dossiers dans le répertoire de sortie (<code>html_output</code>), garantissant que l'architecture est préservée.</li>
  </ul>
</div>

## 🎨 Générateur HTML & Styling CSS

<div class="objective-card dark:bg-white/5 bg-white/80 backdrop-blur-md border dark:border-white/10 border-slate-200 rounded-xl p-6 my-8">
  <p class="text-sm dark:text-white/70 text-slate-600 leading-relaxed mb-4">
    Le script ne se contente pas de convertir le texte ; il produit un fichier <strong>HTML5 complet</strong> et <strong>autonome</strong>. La fonction <code>generate_html</code> encapsule le contenu parsé dans un template HTML, qui inclut une feuille de style <strong>CSS directement intégrée</strong>.
  </p>
  <ul class="list-disc list-outside space-y-2 pl-5 text-sm dark:text-white/70 text-slate-600">
    <li><strong>Template HTML :</strong> Une <code>f-string</code> Python contenant le squelette HTML (<code><!DOCTYPE html></code>, <code><head></code>, <code><body></code>) et insérant dynamiquement le titre.</li>
    <li><strong>CSS Intégré :</strong> Le CSS est défini dans le <code><head></code> à l'intérieur d'une balise <code><style></code>. Cela rend le fichier HTML final portable.</li>
    <li><strong>Design Responsive :</strong> Le CSS utilise des Media Queries (<code>@media (max-width: 600px)</code>) pour adapter l'affichage sur les appareils mobiles.</li>
    <li><strong>Mode Sombre (Dark Mode) :</strong> Le style inclut une règle <code>@media (prefers-color-scheme: dark)</code> qui applique automatiquement un thème sombre.</li>
  </ul>
</div>

## 🎓 Compétences démontrées

<div class="skills-showcase space-y-6 my-8">
  
  <div class="skill-category dark:bg-gradient-to-r dark:from-indigo-900/30 dark:to-purple-900/30 bg-gradient-to-r from-indigo-50 to-purple-50 border dark:border-indigo-500/30 border-indigo-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">⚙️</span>
      <h3 class="text-xl font-bold dark:text-white text-slate-900">Parsing & Expressions Régulières</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Implémentation d'expressions régulières</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Utilisation intensive de `re.sub` pour les remplacements.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Conception de patterns Regex</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Écriture de 13+ patterns (H1-H3, listes, liens, images...).</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Utilisation de groupes de capture</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Extraction de l'URL et du texte (`[texte](url)`) via `(.*?)`.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Parsing avec gestion d'état</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Flag `in_code_block` pour gérer les balises `<pre>` multi-lignes.</div>
        </div>
      </div>
    </div>
  </div>
  
  <div class="skill-category dark:bg-gradient-to-r dark:from-indigo-900/30 dark:to-purple-900/30 bg-gradient-to-r from-indigo-50 to-purple-50 border dark:border-indigo-500/30 border-indigo-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">⌨️</span>
      <h3 class="text-xl font-bold dark:text-white text-slate-900">Développement Outil CLI (Python)</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Gestion d'arguments CLI</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Utilisation du module `argparse` (`--input`, `--output`).</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Interaction avec le système de fichiers</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Fonctions `os.path.isfile`, `os.path.isdir`, `os.makedirs`.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Traitement récursif de dossiers</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Utilisation de `os.walk` pour le traitement par lot.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Lecture et écriture de fichiers</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Gestion propre des fichiers avec encodage `utf-8`.</div>
        </div>
      </div>
    </div>
  </div>

  <div class="skill-category dark:bg-gradient-to-r dark:from-indigo-900/30 dark:to-purple-900/30 bg-gradient-to-r from-indigo-50 to-purple-50 border dark:border-indigo-500/30 border-indigo-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🎨</span>
      <h3 class="text-xl font-bold dark:text-white text-slate-900">Génération Web Statique</h3>
    </div>
    <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Templating HTML (Python natif)</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Utilisation de `f-string` comme moteur de template HTML5.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Intégration CSS</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Injection d'un bloc `<style>` dans le `<head>` (fichier autonome).</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Design Responsive (CSS)</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Implémentation de `@media (max-width: 600px)`.</div>
        </div>
      </div>
      <div class="skill-item flex items-start gap-2 dark:bg-white/5 bg-white/50 rounded-lg p-3">
        <span class="text-green-500 font-bold text-lg">✓</span>
        <div>
          <div class="font-semibold dark:text-white text-slate-900">Support du Thème Sombre (CSS)</div>
          <div class="text-xs dark:text-white/60 text-slate-600">Implémentation de `@media (prefers-color-scheme: dark)`.</div>
        </div>
      </div>
    </div>
  </div>

</div>

## 📚 Ressources & Documentation

<div class="documentation-grid grid grid-cols-1 md:grid-cols-2 gap-6 my-8">
  
  <div class="doc-card dark:bg-gradient-to-br dark:from-slate-900/50 dark:to-slate-800/50 bg-gradient-to-br from-slate-50 to-slate-100 border dark:border-white/10 border-slate-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300 cursor-pointer" data-doc-type="details">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">📖</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">Documentation complète</h3>
    </div>
    <ul class="space-y-3">
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Analyse du code source (mdparser.py)</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Détail des 13+ expressions régulières</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Instructions d'utilisation CLI</span>
      </li>
      <li class="flex items-start gap-2">
        <span class="text-blue-500">▸</span>
        <span class="dark:text-white/70 text-slate-600">Explication du template CSS</span>
      </li>
    </ul>
    <div class="mt-4 text-center">
      <span class="text-sm dark:text-blue-400 text-blue-600 font-semibold">→ Voir les détails techniques</span>
    </div>
  </div>

  <div class="doc-card dark:bg-gradient-to-br dark:from-purple-900/30 dark:to-indigo-900/30 bg-gradient-to-br from-purple-50 to-indigo-50 border dark:border-purple-500/30 border-purple-300 rounded-2xl p-6 hover:scale-[1.02] transition-all duration-300 cursor-pointer" data-doc-type="architecture">
    <div class="flex items-center gap-3 mb-4">
      <span class="text-3xl">🗺️</span>
      <h3 class="text-lg font-bold dark:text-white text-slate-900">Diagramme interactif</h3>
    </div>
    <p class="dark:text-white/70 text-slate-600 mb-4">Visualisation complète de l'architecture avec tooltips détaillés pour chaque composant.</p>
    <div class="flex flex-wrap gap-2 mb-4">
      <span class="px-3 py-1 dark:bg-blue-500/20 bg-blue-200 dark:text-blue-300 text-blue-700 rounded-full text-xs">CLI (Argparse)</span>
      <span class="px-3 py-1 dark:bg-red-500/20 bg-red-200 dark:text-red-300 text-red-700 rounded-full text-xs">Moteur Regex</span>
      <span class="px-3 py-1 dark:bg-purple-500/20 bg-purple-200 dark:text-purple-300 text-purple-700 rounded-full text-xs">Génération HTML</span>
      <span class="px-3 py-1 dark:bg-green-500/20 bg-green-200 dark:text-green-300 text-green-700 rounded-full text-xs">Système de fichiers</span>
    </div>
    <div class="text-center">
      <span class="text-sm dark:text-purple-400 text-purple-600 font-semibold">→ Voir l'architecture</span>
    </div>
  </div>

</div>

<script is:inline>
  document.addEventListener('DOMContentLoaded', function() {
    const docCards = document.querySelectorAll('[data-doc-type]');
    docCards.forEach(card => {
      card.addEventListener('click', function() {
        const type = this.getAttribute('data-doc-type');
        const tabButton = document.querySelector(`[data-tab="${type}"]`);
        if (tabButton) {
          tabButton.click();
        }
      });
    });
  });
</script>

---

**Archivé** | **Outil CLI** | **Projet Académique (ESGI)**
