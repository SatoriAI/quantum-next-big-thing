# Learning: podstawy obliczeń kwantowych

Krótki kurs podstaw, w języku algebry liniowej. Stany to wektory w ℂ^(2ⁿ), bramki to macierze unitarne, a notacja Diraca pojawia się tylko jako etykiety (tak opisują wyniki PennyLane i Qiskit).

Każda lekcja to notebook z teorią, kodem w NumPy, rysunkami i zadaniami. Fragmenty oznaczone „To było trudne” zbierają miejsca, w których najłatwiej o pomyłkę.

| Lekcja | Temat |
|---|---|
| [01_stan_kubitu](01_stan_kubitu.ipynb) | układ dwupoziomowy, transmon, chłodzenie, stan jako wektor w ℂ², kubit vs stan vs wynik |
| [02_pomiar_regula_borna](02_pomiar_regula_borna.ipynb) | reguła Borna, shoty, błąd 1/√N, kolaps, pomiar to nie odczyt |
| [03_bazy_i_faza](03_bazy_i_faza.ipynb) | słownik Dirac → algebra, pomiar w dowolnej bazie, faza globalna i względna, interferencja |
| [04_sfera_blocha](04_sfera_blocha.ipynb) | parametryzacja (θ, φ), osie jako bazy, pomiar jako rzut, α i β przez kąty |
| [05_bramki_i_obwody](05_bramki_i_obwody.ipynb) | unitarność, X, Z, H, obroty, obwód jako iloczyn macierzy, fizyka impulsów |
| [06_wiele_kubitow_i_superpozycja](06_wiele_kubitow_i_superpozycja.ipynb) | ℂ^(2ⁿ) i iloczyn Kroneckera, indeksowanie bitami, definicja superpozycji |
| [07_splatanie_i_stan_bella](07_splatanie_i_stan_bella.ipynb) | stan Bella krok po kroku, test wyznacznika, korelacje w każdej bazie, wynik z ibm_fez |
| [08_bell_w_numpy](08_bell_w_numpy.ipynb) | ćwiczenie: stan Bella zbudowany ręcznie z macierzy i 1000 shotów |
| [09_algorytm_grovera](09_algorytm_grovera.ipynb) | wyrocznia jako macierz diagonalna i z bramek, phase kickback, dyfuzja jako odbicie względem średniej, obrót o 2θ, skąd √N, wyniki z ibm_marrakesh |

## Big picture

Schładzamy układ fizyczny, żeby był nadprzewodnikiem i startował w stanie podstawowym e₀ ⊗ … ⊗ e₀. Impulsami mikrofalowymi obracamy jego stan, co matematycznie jest mnożeniem wektora stanu przez macierze unitarne. Na końcu mierzymy i dostajemy jeden ciąg bitów, losowany według reguły Borna. Całość powtarzamy wiele razy, żeby poznać rozkład. Algorytm kwantowy to dobór obrotów tak, żeby rozkład był skupiony na dobrej odpowiedzi.

## Słownik

| Dirac | Algebra liniowa |
|---|---|
| \|0⟩, \|1⟩ | e₀ = (1, 0), e₁ = (0, 1) |
| \|ab⟩ | e_a ⊗ e_b = e_(2a+b), np. \|10⟩ = e₂ |
| ⟨φ\|ψ⟩ | iloczyn skalarny u*v |
| \|ψ⟩⟨ψ\| | macierz v v* (rzut) |
| U\|ψ⟩ | Uv |

## Uruchamianie

Notebooki wymagają tylko NumPy i matplotlib (są w środowisku projektu: `uv sync`). Wyniki komórek są zapisane w plikach, więc można je czytać bez uruchamiania, także na GitHubie.

Możliwe dalsze tematy: kernele kwantowe (Demo 2) i szum na prawdziwym sprzęcie.
