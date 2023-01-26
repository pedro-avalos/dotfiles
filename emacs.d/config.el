;; NOTE: init.el is gnerated from config.org. Edit config.org, not init.el.

(require 'package)
(setq package-archives '(("melpa" . "https://melpa.org/packages/")
			 ("org" . "https://orgmode.org/elpa/")
			 ("elpa" . "https://elpa.gnu.org/packages/")))

(package-initialize)
(unless package-archive-contents
  (package-refresh-contents))

(unless (package-installed-p 'use-package)
  (package-install 'use-package))

(require 'use-package)
(setq use-package-always-ensure t)

;; Move everything out of the ~/.emacs.d folder
(setq user-emacs-directory "~/.cache/emacs")

(use-package no-littering)

;; Place auto save files into the same path as it uses for sessions
(setq auto-save-file-name-transforms
      `((".*" ,(no-littering-expand-var-file-name "auto-save/") t)))

(setq inhibit-startup-message t) ; Don't show startup message

(menu-bar-mode -1)   ; Disable visible scroll bar
(tool-bar-mode -1)   ; Disable the toolbar
(tooltip-mode -1)    ; Disable tooltips
(set-fringe-mode 10) ; Some extra space on the gutter/fringe
(scroll-bar-mode -1) ; Disable menu bar

(column-number-mode)                 ; Show column numbers
(global-display-line-numbers-mode 1) ; Show line numbers

(global-visual-line-mode t) ; Word wrap

;; Don't show line numbers in these modes
(dolist (mode '(org-mode-hook
		term-mode-hook
		shell-mode-hook
		eshell-mode-hook))
  (add-hook mode (lambda () (display-line-numbers-mode 0))))

(add-to-list 'custom-theme-load-path "~/.emacs.d/themes/")
(load-theme 'catppuccin t)
(setq catppuccin-flavor 'mocha)
(catppuccin-reload)

(use-package all-the-icons
  :if (display-graphic-p))
(use-package doom-modeline
  :init (doom-modeline-mode 1)
  :custom ((doom-modeline-height 15)))

;; Set up evil mode
(use-package evil
  :init
  (setq evil-want-integration t)
  (setq evil-want-keybinding nil)
  (setq evil-vsplit-window-right t)
  (setq evil-split-window-below t)
  (evil-mode))

;; Add evil keybindings to more modes
(use-package evil-collection
  :after evil
  :config
  (setq evil-collection-mode-list '(dashboard dired ibuffer))
  (evil-collection-init))

;; Use evil keybindings
(use-package general
  :config
  (general-evil-setup t))

;; Evil mode tutorial
(use-package evil-tutor)
