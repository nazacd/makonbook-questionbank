# Changes to SAT MAKON's vocabulary list

Source: SAT MAKON's `sat_vocabularyword.csv` (1,250 rows, all active, exported 2026-04-02), columns `id, word, meaning, example, is_active, created_at, unit_id`. This file lists every change made to it for `words.jsonl`. `python3 tools/check_vocab.py` validates the result.

## Summary

- **1,250 rows in, 1,220 words out**, in 50 lists (25 duplicates and 5 rows that are not vocabulary removed; see below).
- **Words:** 233 words fixed: 159 capital letter, 37 leading article, 41 PDF ligature, 1 wrong word, 4 broken character (some words had two fixes). Every fix is in the table below. The words themselves are SAT MAKON's.
- **Definitions:** 1,185 kept as SAT MAKON wrote them, 35 rewritten (table below). In 196 of the kept ones, PDF ligature characters (ﬁ ﬂ ﬀ ﬃ ﬄ) were replaced by plain letters; the wording is unchanged.
- **Examples:** SAT MAKON's file has none, so all 1,220 are new: one sentence each, using the word itself or a simple inflection, with no names of real people.
- **Part of speech:** added for every word, as its definition uses it. A participle that the definition treats as a verb form ("overshadowed by: made less important…") is a verb; one it treats as a description ("cherished: greatly valued and loved") is an adjective. A word with a preposition after it takes the part of speech of the word ("skepticism toward": noun).

- **Pictures:** 130 words have one (see Pictures below); the others have no `image` field.

## Lists

SAT MAKON's file groups the words into 50 units of 25 (`unit_id` 159–208), and `id` follows the same order. Each unit is one list, in the same order and named after its position: `unit_id` 159 is `sat-unit-1`, "SAT Words: Unit 1", up to `unit_id` 208, `sat-unit-50`, "SAT Words: Unit 50". Within a list, words are in the file's order (by `id`).

Lists that lost a word to the removals below: Unit 12 (24), Unit 20 (23), Unit 22 (24), Unit 26 (24), Unit 29 (23), Unit 30 (23), Unit 34 (24), Unit 35 (24), Unit 36 (22), Unit 47 (24), Unit 48 (24), Unit 50 (11). All others have 25 words.

## Word fixes

What each fix means:

- **PDF ligature:** the export kept the single characters ﬁ ﬂ ﬀ ﬃ ﬄ, which look right but do not match the real letters in search or spell-check. Replaced by the letters.
- **broken character:** `!` or `”` where the PDF had ff or ffi (o!ered → offered, a”nity → affinity).
- **capital letter:** the word was copied from the start of an answer choice ("Cherished"). Lower-cased; none of them is a proper noun.
- **leading article:** "a" or "an" was copied along with the word from an answer choice ("an accessory", "a prudently"). Removed, because it is not part of the word. This made 10 entries duplicates of other entries (see Duplicates).
- **wrong word:** "appraised of" is a common slip for "apprised of". The definition is the definition of "apprised of".

A preposition after a word ("skepticism toward", "adept at") is kept: the SAT tests these pairs, and SAT MAKON's definitions are written for them.

| List | id | SAT MAKON's word | Now | Fix |
|---|---|---|---|---|
| Unit 1 | 2541 | Cherished | cherished | capital letter |
| Unit 1 | 2546 | an accessory | accessory | leading article |
| Unit 2 | 2554 | Vague | vague | capital letter |
| Unit 2 | 2557 | Disorganized | disorganized | capital letter |
| Unit 2 | 2560 | An extraordinary | extraordinary | leading article |
| Unit 2 | 2570 | Lift | lift | capital letter |
| Unit 3 | 2584 | Described | described | capital letter |
| Unit 3 | 2585 | ﬁneness | fineness | PDF ligature |
| Unit 3 | 2586 | Emulate | emulate | capital letter |
| Unit 3 | 2587 | an oddity | oddity | leading article |
| Unit 3 | 2592 | Tenderly | tenderly | capital letter |
| Unit 3 | 2598 | Standard | standard | capital letter |
| Unit 3 | 2601 | Ranked | ranked | capital letter |
| Unit 4 | 2612 | Reveal | reveal | capital letter |
| Unit 4 | 2615 | appraised of | apprised of | wrong word: "appraised" means valued; the definition ("informed or made aware of") is "apprised of" |
| Unit 4 | 2621 | Entering | entering | capital letter |
| Unit 4 | 2624 | an incident | incident | leading article |
| Unit 4 | 2627 | Correct | correct | capital letter |
| Unit 5 | 2632 | Stretching toward | stretching toward | capital letter |
| Unit 5 | 2638 | Joining with | joining with | capital letter |
| Unit 5 | 2643 | Basic | basic | capital letter |
| Unit 5 | 2648 | Abruptly | abruptly | capital letter |
| Unit 5 | 2649 | Accomplishment | accomplishment | capital letter |
| Unit 5 | 2650 | An incomplete | incomplete | leading article |
| Unit 6 | 2669 | Bypassed | bypassed | capital letter |
| Unit 6 | 2672 | Particular | particular | capital letter |
| Unit 7 | 2684 | Create | create | capital letter |
| Unit 7 | 2687 | Advertising | advertising | capital letter |
| Unit 7 | 2688 | Enough | enough | capital letter |
| Unit 7 | 2690 | Suspicious | suspicious | capital letter |
| Unit 7 | 2691 | a determined | determined | leading article |
| Unit 7 | 2693 | Arriving at | arriving at | capital letter |
| Unit 7 | 2699 | Inspired | inspired | capital letter |
| Unit 7 | 2700 | Trace | trace | capital letter |
| Unit 7 | 2701 | an explanation | explanation | leading article |
| Unit 7 | 2703 | inﬂuenced | influenced | PDF ligature |
| Unit 8 | 2707 | Dictate | dictate | capital letter |
| Unit 8 | 2708 | Persuade | persuade | capital letter |
| Unit 8 | 2710 | an imaginative | imaginative | leading article |
| Unit 8 | 2712 | Sketch | sketch | capital letter |
| Unit 8 | 2715 | a questionable | questionable | leading article |
| Unit 8 | 2717 | Insuperable | insuperable | capital letter |
| Unit 8 | 2726 | Visualize | visualize | capital letter |
| Unit 9 | 2729 | Fulﬁlls | fulfills | PDF ligature; capital letter |
| Unit 9 | 2731 | Irreproachable | irreproachable | capital letter |
| Unit 9 | 2734 | Conveyed | conveyed | capital letter |
| Unit 9 | 2736 | Gaining on | gaining on | capital letter |
| Unit 9 | 2737 | an unbiased | unbiased | leading article |
| Unit 9 | 2739 | conﬂated with | conflated with | PDF ligature |
| Unit 9 | 2746 | oﬀered | offered | PDF ligature |
| Unit 9 | 2751 | Repeatedly | repeatedly | capital letter |
| Unit 10 | 2755 | oﬀhand | offhand | PDF ligature |
| Unit 10 | 2765 | Enrolled | enrolled | capital letter |
| Unit 10 | 2768 | Choose | choose | capital letter |
| Unit 10 | 2770 | a”nity for | affinity for | broken character |
| Unit 10 | 2772 | Inviting | inviting | capital letter |
| Unit 11 | 2781 | Settled | settled | capital letter |
| Unit 11 | 2790 | Rebuts | rebuts | capital letter |
| Unit 12 | 2804 | Consulting with | consulting with | capital letter |
| Unit 12 | 2820 | beneﬁciary of | beneficiary of | PDF ligature |
| Unit 12 | 2823 | Urge | urge | capital letter |
| Unit 13 | 2830 | Anticipated | anticipated | capital letter |
| Unit 13 | 2837 | Staged | staged | capital letter |
| Unit 13 | 2838 | an arduous | arduous | leading article |
| Unit 13 | 2841 | unclassiﬁable | unclassifiable | PDF ligature |
| Unit 13 | 2844 | Protective | protective | capital letter |
| Unit 13 | 2848 | ﬂuctuate | fluctuate | PDF ligature |
| Unit 13 | 2850 | Ignored | ignored | capital letter |
| Unit 14 | 2869 | Accurate | accurate | capital letter |
| Unit 14 | 2872 | an inadvertently | inadvertently | leading article |
| Unit 14 | 2873 | Persist | persist | capital letter |
| Unit 15 | 2881 | Clinging to | clinging to | capital letter |
| Unit 15 | 2890 | beneﬁcial | beneficial | PDF ligature |
| Unit 15 | 2892 | Looking forward to | looking forward to | capital letter |
| Unit 15 | 2895 | Characteristic | characteristic | capital letter |
| Unit 15 | 2901 | a coincidence | coincidence | leading article |
| Unit 16 | 2904 | Developed | developed | capital letter |
| Unit 16 | 2909 | Carrying | carrying | capital letter |
| Unit 16 | 2910 | redeﬁned | redefined | PDF ligature |
| Unit 16 | 2925 | reﬂect | reflect | PDF ligature |
| Unit 17 | 2931 | deﬁnite | definite | PDF ligature |
| Unit 17 | 2933 | exempliﬁes | exemplifies | PDF ligature |
| Unit 17 | 2936 | Fragile | fragile | capital letter |
| Unit 17 | 2949 | a superﬁcial | superficial | PDF ligature; leading article |
| Unit 17 | 2951 | Asserting possession of | asserting possession of | capital letter |
| Unit 18 | 2954 | A forgotten | forgotten | leading article |
| Unit 18 | 2957 | Transparent | transparent | capital letter |
| Unit 18 | 2960 | Command | command | capital letter |
| Unit 18 | 2962 | a haphazard | haphazard | leading article |
| Unit 18 | 2964 | an exhaustive | exhaustive | leading article |
| Unit 18 | 2966 | Harsh | harsh | capital letter |
| Unit 18 | 2967 | Drained | drained | capital letter |
| Unit 18 | 2970 | a repudiation | repudiation | leading article |
| Unit 18 | 2973 | Alarmed | alarmed | capital letter |
| Unit 18 | 2974 | ﬂuctuate with | fluctuate with | PDF ligature |
| Unit 19 | 2981 | eﬃcacy | efficacy | PDF ligature |
| Unit 19 | 2987 | An empty | empty | leading article |
| Unit 19 | 2991 | indiﬀerence to | indifference to | PDF ligature |
| Unit 19 | 2992 | Prestige | prestige | capital letter |
| Unit 19 | 2994 | Arranged | arranged | capital letter |
| Unit 19 | 2995 | Disguise | disguise | capital letter |
| Unit 19 | 2999 | Explains | explains | capital letter |
| Unit 19 | 3001 | di!erent from | different from | broken character |
| Unit 20 | 3004 | a reprieve | reprieve | leading article |
| Unit 20 | 3005 | Revealing | revealing | capital letter |
| Unit 20 | 3007 | Tolerate | tolerate | capital letter |
| Unit 20 | 3008 | conﬁdent | confident | PDF ligature |
| Unit 20 | 3009 | Defends | defends | capital letter |
| Unit 20 | 3012 | Pulled | pulled | capital letter |
| Unit 20 | 3025 | a contradiction | contradiction | leading article |
| Unit 21 | 3040 | Judge | judge | capital letter |
| Unit 21 | 3042 | beneﬁcially | beneficially | PDF ligature |
| Unit 21 | 3044 | Improved on | improved on | capital letter |
| Unit 21 | 3045 | Shapeless | shapeless | capital letter |
| Unit 21 | 3048 | Acknowledged | acknowledged | capital letter |
| Unit 22 | 3054 | Voluntarily | voluntarily | capital letter |
| Unit 22 | 3063 | proﬁcient | proficient | PDF ligature |
| Unit 22 | 3067 | Speculated | speculated | capital letter |
| Unit 22 | 3070 | Vacate | vacate | capital letter |
| Unit 22 | 3072 | Running to | running to | capital letter |
| Unit 22 | 3073 | an acceptable | acceptable | leading article |
| Unit 22 | 3074 | Teach | teach | capital letter |
| Unit 23 | 3082 | Follows | follows | capital letter |
| Unit 23 | 3083 | a disconcerting | disconcerting | leading article |
| Unit 23 | 3095 | Scratchy | scratchy | capital letter |
| Unit 24 | 3109 | a straightforward | straightforward | leading article |
| Unit 24 | 3116 | Celebrated | celebrated | capital letter |
| Unit 25 | 3129 | A disagreeable | disagreeable | leading article |
| Unit 25 | 3133 | Faintly | faintly | capital letter |
| Unit 25 | 3137 | Rejecting | rejecting | capital letter |
| Unit 25 | 3138 | a discernible | discernible | leading article |
| Unit 25 | 3143 | Easily | easily | capital letter |
| Unit 26 | 3172 | Restrictive | restrictive | capital letter |
| Unit 26 | 3173 | a prudently | prudently | leading article |
| Unit 26 | 3176 | Passes | passes | capital letter |
| Unit 27 | 3180 | di!er from | differ from | broken character |
| Unit 27 | 3184 | Hearing | hearing | capital letter |
| Unit 27 | 3189 | Getting ahead of | getting ahead of | capital letter |
| Unit 28 | 3209 | Regret | regret | capital letter |
| Unit 28 | 3212 | Visible | visible | capital letter |
| Unit 28 | 3222 | Generous | generous | capital letter |
| Unit 28 | 3224 | Discussed | discussed | capital letter |
| Unit 28 | 3227 | Demanding | demanding | capital letter |
| Unit 28 | 3228 | Demonstrate | demonstrate | capital letter |
| Unit 29 | 3229 | Organized | organized | capital letter |
| Unit 29 | 3231 | exempliﬁcations | exemplifications | PDF ligature |
| Unit 29 | 3233 | Carefully | carefully | capital letter |
| Unit 29 | 3238 | an ineﬀectual | ineffectual | PDF ligature; leading article |
| Unit 29 | 3243 | an overtly | overtly | leading article |
| Unit 29 | 3245 | Possible | possible | capital letter |
| Unit 29 | 3246 | ﬂuctuations in | fluctuations in | PDF ligature |
| Unit 30 | 3255 | Combined | combined | capital letter |
| Unit 30 | 3257 | Simple | simple | capital letter |
| Unit 30 | 3263 | Steady | steady | capital letter |
| Unit 30 | 3264 | Strengthen | strengthen | capital letter |
| Unit 31 | 3280 | Watched | watched | capital letter |
| Unit 31 | 3285 | Easy | easy | capital letter |
| Unit 31 | 3298 | Signaling | signaling | capital letter |
| Unit 31 | 3299 | preﬁguring | prefiguring | PDF ligature |
| Unit 32 | 3306 | Contracted | contracted | capital letter |
| Unit 32 | 3310 | deﬁed | defied | PDF ligature |
| Unit 32 | 3315 | ineﬀective | ineffective | PDF ligature |
| Unit 32 | 3316 | eﬃcient | efficient | PDF ligature |
| Unit 32 | 3328 | Oﬀended | offended | PDF ligature; capital letter |
| Unit 33 | 3337 | Nonstop | nonstop | capital letter |
| Unit 33 | 3338 | a suitable | suitable | leading article |
| Unit 33 | 3342 | Converted | converted | capital letter |
| Unit 33 | 3344 | a cordially | cordially | leading article |
| Unit 34 | 3362 | Marks | marks | capital letter |
| Unit 34 | 3364 | Enjoyed | enjoyed | capital letter |
| Unit 34 | 3366 | Mislead | mislead | capital letter |
| Unit 34 | 3375 | Held up | held up | capital letter |
| Unit 35 | 3380 | Foolishly | foolishly | capital letter |
| Unit 35 | 3388 | Interrupted | interrupted | capital letter |
| Unit 35 | 3392 | superﬂuous | superfluous | PDF ligature |
| Unit 35 | 3397 | Spectacle | spectacle | capital letter |
| Unit 36 | 3404 | reﬁnements of | refinements of | PDF ligature |
| Unit 36 | 3406 | Displayed | displayed | capital letter |
| Unit 36 | 3411 | Finishing | finishing | capital letter |
| Unit 36 | 3414 | Select | select | capital letter |
| Unit 36 | 3419 | Unequivocal | unequivocal | capital letter |
| Unit 37 | 3430 | Amount | amount | capital letter |
| Unit 37 | 3431 | Gentle | gentle | capital letter |
| Unit 37 | 3436 | Identiﬁed | identified | PDF ligature; capital letter |
| Unit 37 | 3439 | Approved | approved | capital letter |
| Unit 37 | 3443 | solidiﬁed | solidified | PDF ligature |
| Unit 37 | 3450 | Inﬂuence | influence | PDF ligature; capital letter |
| Unit 37 | 3451 | Providing resistance to | providing resistance to | capital letter |
| Unit 38 | 3454 | Destroying | destroying | capital letter |
| Unit 38 | 3456 | di”cult | difficult | broken character |
| Unit 38 | 3463 | Aﬀectionate | affectionate | PDF ligature; capital letter |
| Unit 38 | 3468 | Turns | turns | capital letter |
| Unit 38 | 3471 | Endured | endured | capital letter |
| Unit 38 | 3472 | signiﬁcant | significant | PDF ligature |
| Unit 39 | 3482 | Deﬁne | define | PDF ligature; capital letter |
| Unit 39 | 3488 | Pretentiousness | pretentiousness | capital letter |
| Unit 40 | 3507 | Hastily | hastily | capital letter |
| Unit 40 | 3509 | Measure | measure | capital letter |
| Unit 40 | 3511 | Priced | priced | capital letter |
| Unit 40 | 3513 | Blemish | blemish | capital letter |
| Unit 40 | 3514 | insigniﬁcance | insignificance | PDF ligature |
| Unit 40 | 3515 | Reproduction | reproduction | capital letter |
| Unit 40 | 3525 | Arguing about | arguing about | capital letter |
| Unit 40 | 3526 | Sketched | sketched | capital letter |
| Unit 40 | 3527 | conﬁrm | confirm | PDF ligature |
| Unit 41 | 3529 | Examined | examined | capital letter |
| Unit 41 | 3536 | Hidden | hidden | capital letter |
| Unit 41 | 3549 | Stained | stained | capital letter |
| Unit 42 | 3554 | Shifting | shifting | capital letter |
| Unit 42 | 3555 | Evident | evident | capital letter |
| Unit 42 | 3557 | Ineluctable | ineluctable | capital letter |
| Unit 42 | 3566 | Encourage | encourage | capital letter |
| Unit 42 | 3574 | Denying | denying | capital letter |
| Unit 42 | 3577 | Modiﬁed | modified | PDF ligature; capital letter |
| Unit 42 | 3578 | aﬀecting | affecting | PDF ligature |
| Unit 43 | 3579 | an analogy | analogy | leading article |
| Unit 43 | 3581 | an arbitrary | arbitrary | leading article |
| Unit 43 | 3589 | A lonely | lonely | leading article |
| Unit 43 | 3602 | Defended | defended | capital letter |
| Unit 44 | 3618 | Imaginary | imaginary | capital letter |
| Unit 44 | 3621 | Complimented | complimented | capital letter |
| Unit 44 | 3627 | Congratulate | congratulate | capital letter |
| Unit 45 | 3636 | a contentious | contentious | leading article |
| Unit 45 | 3639 | Valued | valued | capital letter |
| Unit 45 | 3646 | Scheduled | scheduled | capital letter |
| Unit 46 | 3655 | Conclude | conclude | capital letter |
| Unit 46 | 3658 | an imperceptible | imperceptible | leading article |
| Unit 46 | 3674 | an objective | objective | leading article |
| Unit 46 | 3675 | Bland | bland | capital letter |
| Unit 46 | 3678 | Obvious | obvious | capital letter |
| Unit 47 | 3679 | Energetic | energetic | capital letter |
| Unit 47 | 3687 | Managing | managing | capital letter |
| Unit 47 | 3699 | Estimated | estimated | capital letter |

## Removed

### Duplicates

A word that appears twice keeps its first entry. Compared after the fixes above, ignoring case.

| Removed: list, id, SAT MAKON's word | Kept: list, id, word | Note |
|---|---|---|
| Unit 12, 2828, o!ered | Unit 9, 2746, offered |  |
| Unit 20, 3014, imaginative | Unit 8, 2710, imaginative |  |
| Unit 20, 3015, empty | Unit 19, 2987, empty |  |
| Unit 26, 3155, determined | Unit 7, 2691, determined | different sense: Unit 26's entry meant "decided firmly"; the kept entry (Unit 7) means "firmly resolved" |
| Unit 29, 3242, a collaboration | Unit 17, 2940, collaboration |  |
| Unit 30, 3273, haphazard | Unit 18, 2962, haphazard |  |
| Unit 30, 3274, A useless | Unit 26, 3178, useless |  |
| Unit 34, 3370, an inconclusive | Unit 27, 3187, inconclusive |  |
| Unit 35, 3389, a substantial | Unit 15, 2880, substantial |  |
| Unit 36, 3415, an unpredictable | Unit 11, 2784, unpredictable |  |
| Unit 48, 3709, arbitrary | Unit 43, 3581, arbitrary |  |
| Unit 50, 3754, adapt | Unit 49, 3740, adapt |  |
| Unit 50, 3755, apparent | Unit 49, 3741, apparent |  |
| Unit 50, 3756, contradict | Unit 49, 3742, contradict |  |
| Unit 50, 3757, depict | Unit 49, 3743, depict |  |
| Unit 50, 3758, disregard | Unit 49, 3744, disregard |  |
| Unit 50, 3759, exemplify | Unit 49, 3745, exemplify |  |
| Unit 50, 3760, explicit | Unit 49, 3746, explicit |  |
| Unit 50, 3761, flexible | Unit 49, 3747, flexible |  |
| Unit 50, 3762, infer | Unit 49, 3748, infer |  |
| Unit 50, 3763, marginal | Unit 49, 3749, marginal |  |
| Unit 50, 3764, relevant to | Unit 49, 3750, relevant to |  |
| Unit 50, 3765, signify | Unit 49, 3751, signify |  |
| Unit 50, 3766, stable | Unit 49, 3752, stable |  |
| Unit 50, 3767, valid | Unit 49, 3753, valid |  |

Unit 50 repeats 14 of Unit 49's words, in the same order and with the same definitions (ids 3754–3767 repeat 3740–3753).

### Not vocabulary

- Unit 22, id 3077: An answer choice from a reading question, not vocabulary. The row: "Get his mother to accept"
- Unit 29, id 3240: An answer choice from a reading question, not vocabulary. The row: "Get his mother to reunite with"
- Unit 36, id 3420: The word field holds a whole question sentence with a blank instead of a word, and at 113 characters it is over the 100 limit. Its definition ("providing evidence; demonstrating; showing") points to *demonstrating*, which is already in Unit 35 (id 3396). The row: "David de Santana proved this idea wrong by \_\_\_\_\_\_ that there are in fact three distinct species of electric eels."
- Unit 36, id 3421: An answer choice from a reading question, not vocabulary. The row: "Get his mother to match"
- Unit 47, id 3694: An answer choice from a reading question, not vocabulary. The row: "Get his mother to apologize for"

## For SAT MAKON to look at

- The same word is in the list both alone and in a longer entry, usually with a preposition. Both are kept: they are different entries in SAT MAKON's file, not duplicates. Merge them if you prefer one card per word:

  | Word | List | Longer entry | List |
  |---|---|---|---|
  | ambivalence | Unit 9 | ambivalence toward | Unit 2 |
  | useful | Unit 26 | useful to | Unit 5 |
  | confused | Unit 22 | confused with | Unit 10 |
  | controversial | Unit 48 | controversial among | Unit 11 |
  | doubts | Unit 37 | doubts about | Unit 11 |
  | adapt | Unit 49 | adapt to | Unit 12 |
  | irrelevant | Unit 10 | irrelevant to | Unit 12 |
  | collected | Unit 43 | collected with | Unit 13 |
  | imitated | Unit 8 | imitated by | Unit 14 |
  | motivation | Unit 10 | motivation for | Unit 16 |
  | consistent | Unit 19 | consistent with | Unit 16 |
  | fluctuate | Unit 13 | fluctuate with | Unit 18 |
  | depleted | Unit 2 | depleted of | Unit 20 |
  | independent | Unit 47 | independent of | Unit 21 |
  | uncertain | Unit 24 | uncertain about | Unit 24 |
  | question | Unit 6 | question about | Unit 25 |
  | complicated | Unit 25 | complicated by | Unit 25 |
  | constrain | Unit 48 | constrain within | Unit 27 |
  | developed | Unit 16 | developed into | Unit 30 |
  | controversy | Unit 22 | controversy in | Unit 31 |
  | unsympathetic | Unit 34 | unsympathetic to | Unit 32 |
  | collaboration | Unit 17 | collaboration between | Unit 33 |
  | precursors | Unit 6 | precursors of | Unit 33 |
  | controversy | Unit 22 | controversy over | Unit 33 |
  | representative | Unit 35 | representative of | Unit 38 |
  | experiment | Unit 26 | experiment with | Unit 40 |
  | inconsequential | Unit 11 | inconsequential to | Unit 42 |
  | complimented | Unit 44 | complimented by | Unit 43 |
  | prevail | Unit 46 | prevail over | Unit 43 |
  | attractive | Unit 21 | attractive to | Unit 44 |
  | reserved | Unit 12 | reserved for | Unit 47 |
  | inspired | Unit 7 | inspired by | Unit 47 |
  | infer | Unit 49 | infer from | Unit 48 |
  | reveal | Unit 4 | reveal about | Unit 48 |
  | skeptical | Unit 25 | skeptical of | Unit 48 |
  | compelling | Unit 18 | compelling evidence | Unit 48 |

## Pictures

130 words have an `image`: an 800×800 PNG in `vocab/images/` named after the word. The first 30 were picked as the easiest to show in a picture; the other 100 were drawn in batches of 50, each time the first 50 words of `vocab/image-prompts/prompts.jsonl`, in study order, that had none. They are flat illustrations drawn for this list (not photos and not from SAT MAKON), with no text in them, so the picture shows the meaning and the app shows the word.

| List | Word | Picture |
|---|---|---|
| Unit 1 | skepticism toward | `skepticism-toward.png` |
| Unit 1 | careful | `careful.png` |
| Unit 1 | assistance | `assistance.png` |
| Unit 1 | scrutinize | `scrutinize.png` |
| Unit 1 | restricted | `restricted.png` |
| Unit 1 | cherished | `cherished.png` |
| Unit 1 | enthusiasm for | `enthusiasm-for.png` |
| Unit 1 | publicity | `publicity.png` |
| Unit 1 | overshadowed by | `overshadowed-by.png` |
| Unit 1 | surprise at | `surprise-at.png` |
| Unit 2 | vague | `vague.png` |
| Unit 2 | struggling | `struggling.png` |
| Unit 2 | disorganized | `disorganized.png` |
| Unit 2 | nurture | `nurture.png` |
| Unit 2 | advice | `advice.png` |
| Unit 2 | depleted | `depleted.png` |
| Unit 2 | inspect | `inspect.png` |
| Unit 2 | lift | `lift.png` |
| Unit 2 | overlooked | `overlooked.png` |
| Unit 2 | evidence | `evidence.png` |
| Unit 3 | buttress | `buttress.png` |
| Unit 3 | profusion of | `profusion-of.png` |
| Unit 3 | emulate | `emulate.png` |
| Unit 3 | oddity | `oddity.png` |
| Unit 3 | collaborators | `collaborators.png` |
| Unit 3 | secretive | `secretive.png` |
| Unit 3 | tenderly | `tenderly.png` |
| Unit 3 | decorations | `decorations.png` |
| Unit 3 | replicate | `replicate.png` |
| Unit 3 | abandon | `abandon.png` |
| Unit 4 | ornamental | `ornamental.png` |
| Unit 4 | attract | `attract.png` |
| Unit 4 | imitation | `imitation.png` |
| Unit 4 | refusing | `refusing.png` |
| Unit 4 | reveal | `reveal.png` |
| Unit 4 | mimicked | `mimicked.png` |
| Unit 4 | anomaly | `anomaly.png` |
| Unit 4 | reciprocates | `reciprocates.png` |
| Unit 4 | acclaim | `acclaim.png` |
| Unit 4 | conspicuous | `conspicuous.png` |
| Unit 5 | recognize | `recognize.png` |
| Unit 5 | stretching toward | `stretching-toward.png` |
| Unit 5 | partnership | `partnership.png` |
| Unit 5 | thrive | `thrive.png` |
| Unit 5 | rapid | `rapid.png` |
| Unit 5 | surpassed by | `surpassed-by.png` |
| Unit 5 | abruptly | `abruptly.png` |
| Unit 5 | accomplishment | `accomplishment.png` |
| Unit 5 | incomplete | `incomplete.png` |
| Unit 5 | achievements | `achievements.png` |
| Unit 6 | observant | `observant.png` |
| Unit 6 | content | `content.png` |
| Unit 6 | fruitless | `fruitless.png` |
| Unit 6 | precursors | `precursors.png` |
| Unit 6 | bypassed | `bypassed.png` |
| Unit 6 | ignore | `ignore.png` |
| Unit 6 | source | `source.png` |
| Unit 6 | rejected | `rejected.png` |
| Unit 6 | appeased | `appeased.png` |
| Unit 6 | inherited | `inherited.png` |
| Unit 7 | rival | `rival.png` |
| Unit 7 | worried | `worried.png` |
| Unit 7 | create | `create.png` |
| Unit 7 | amplify | `amplify.png` |
| Unit 7 | suspicious | `suspicious.png` |
| Unit 7 | determined | `determined.png` |
| Unit 7 | praised | `praised.png` |
| Unit 7 | improvise | `improvise.png` |
| Unit 7 | trace | `trace.png` |
| Unit 7 | alter | `alter.png` |
| Unit 8 | anticipating | `anticipating.png` |
| Unit 8 | persuade | `persuade.png` |
| Unit 8 | imaginative | `imaginative.png` |
| Unit 8 | sketch | `sketch.png` |
| Unit 8 | imitated | `imitated.png` |
| Unit 8 | exposed | `exposed.png` |
| Unit 8 | subdued | `subdued.png` |
| Unit 8 | catastrophic | `catastrophic.png` |
| Unit 8 | craft | `craft.png` |
| Unit 8 | visualize | `visualize.png` |
| Unit 9 | hoard | `hoard.png` |
| Unit 9 | gaining on | `gaining-on.png` |
| Unit 9 | exaggerate | `exaggerate.png` |
| Unit 9 | reconcile | `reconcile.png` |
| Unit 9 | paucity of | `paucity-of.png` |
| Unit 9 | refute | `refute.png` |
| Unit 9 | offered | `offered.png` |
| Unit 9 | costly | `costly.png` |
| Unit 9 | surrendered | `surrendered.png` |
| Unit 9 | dormant | `dormant.png` |
| Unit 10 | powerful | `powerful.png` |
| Unit 10 | discovered | `discovered.png` |
| Unit 10 | focused | `focused.png` |
| Unit 10 | extended | `extended.png` |
| Unit 10 | insurmountable | `insurmountable.png` |
| Unit 10 | choose | `choose.png` |
| Unit 10 | affinity for | `affinity-for.png` |
| Unit 10 | inviting | `inviting.png` |
| Unit 10 | clashed with | `clashed-with.png` |
| Unit 10 | accelerate | `accelerate.png` |
| Unit 11 | partition | `partition.png` |
| Unit 11 | deceptive | `deceptive.png` |
| Unit 11 | magnify | `magnify.png` |
| Unit 11 | unpredictable | `unpredictable.png` |
| Unit 11 | renounce | `renounce.png` |
| Unit 11 | oversees | `oversees.png` |
| Unit 11 | interdependent | `interdependent.png` |
| Unit 13 | fluctuate | `fluctuate.png` |
| Unit 13 | accumulate | `accumulate.png` |
| Unit 17 | dissolve | `dissolve.png` |
| Unit 17 | fragile | `fragile.png` |
| Unit 18 | transparent | `transparent.png` |
| Unit 19 | abundant | `abundant.png` |
| Unit 20 | homogeneous | `homogeneous.png` |
| Unit 20 | hibernation | `hibernation.png` |
| Unit 20 | diverge | `diverge.png` |
| Unit 21 | isolate | `isolate.png` |
| Unit 24 | obstructed | `obstructed.png` |
| Unit 25 | multiplying | `multiplying.png` |
| Unit 27 | heterogeneous | `heterogeneous.png` |
| Unit 28 | constrict | `constrict.png` |
| Unit 31 | erratic | `erratic.png` |
| Unit 33 | immense | `immense.png` |
| Unit 36 | converge | `converge.png` |
| Unit 38 | meager | `meager.png` |
| Unit 40 | dispersed | `dispersed.png` |
| Unit 46 | tranquil | `tranquil.png` |
| Unit 47 | intersect | `intersect.png` |
| Unit 50 | withstand | `withstand.png` |
| Unit 50 | ephemeral | `ephemeral.png` |

## Definitions rewritten

SAT MAKON's definitions use one style: a short definition, then synonyms, separated by semicolons. A definition was kept when it is correct, clear and fits the word as listed. It was rewritten (in the same style) when it was wrong or misleading, gave a sense the SAT rarely tests, mixed parts of speech, or repeated a synonym or the word itself.

| List | Word | SAT MAKON's definition | New definition | Why |
|---|---|---|---|---|
| Unit 3 | approximate | nearly correct or exact; estimate; approach | close to the actual amount but not exact; rough; estimated | mixed the adjective with verb synonyms ("estimate; approach") |
| Unit 6 | universal | done by all people; worldwide; global | true for or shared by everyone or everything; worldwide; general | "done by all people" is not what the word means |
| Unit 6 | particular | specific or distinct; specific; individual | relating to one specific person or thing; specific; individual | "specific" was listed twice |
| Unit 8 | craft | skill or to make skillfully; create; build | to make or shape something with skill and care; create; build | mixed the noun ("skill") and the verb in one definition |
| Unit 9 | conflated with | combined with; merged; blended | wrongly treated as the same as something else; confused with; mixed up with | missed the key idea that the two things are wrongly treated as one |
| Unit 14 | interjected | inserted or interrupted; interrupted; added | said something suddenly while someone else was speaking; interrupted; cut in | "interrupted" was listed twice and "inserted" is unclear |
| Unit 15 | compound | make more intense or combine; combine; intensify | to make a problem worse by adding to it; worsen; intensify | unclear mix of senses; the SAT sense is "make a problem worse" |
| Unit 19 | efficacy | effectiveness; efficiency; usefulness | the ability to produce the intended result; effectiveness; power | "efficiency" is a different word, often confused with efficacy |
| Unit 20 | hibernation | a period of inactivity; dormancy; torpor | the long, sleep-like state in which some animals spend the winter; dormancy; inactivity | too vague ("a period of inactivity"); "torpor" is not a plain word |
| Unit 23 | borrow | to take and use temporarily; loan; take | to take and use something that belongs to someone else, such as an idea; take; adopt | "loan" means the opposite (to lend) |
| Unit 26 | contributions to | things given for a purpose; donations; offerings | things done or given that help something succeed or develop; additions; donations | did not cover the common academic sense ("her contributions to science") |
| Unit 26 | suspect | to think something is likely; doubt; distrust | to think something is probably true, without being sure; believe; guess | the synonyms "doubt; distrust" contradicted the definition |
| Unit 26 | restrictive | limiting; confining; limiting | keeping someone or something within strict limits; limiting; confining | "limiting" was listed twice |
| Unit 27 | hearing | the ability to perceive sound; listening; audition | the ability to hear sounds; sense of sound; listening | "audition" usually means a performance test, not hearing |
| Unit 28 | prohibitive | preventing something; restrictive; forbidding | so high or severe that it stops people from doing or buying something; unaffordable; restrictive | missed the SAT sense ("a prohibitive cost") |
| Unit 30 | speculates | thinks about possible causes; guesses; hypothesizes | forms ideas about something without firm evidence; guesses; hypothesizes | "thinks about possible causes" was too narrow |
| Unit 31 | watched | observed; observed; viewed | looked at carefully for a period of time; observed; viewed | "observed" was listed twice |
| Unit 31 | misconstrued | misunderstood; misinterpreted; misunderstood | understood in the wrong way; misinterpreted; misread | "misunderstood" was listed twice |
| Unit 31 | signaling | giving a sign or signal; indicating; signaling | showing or suggesting something by a sign or action; indicating; pointing to | used the word itself ("signaling") as its own synonym |
| Unit 33 | overreach by | try to do too much; exceed limits; go too far | an attempt to do more than is proper or allowed; going too far; excess | defined a verb, but the entry is the noun ("overreach by the government") |
| Unit 33 | confusing for | making something unclear; baffling to; perplexing for | hard for someone to understand; baffling to; perplexing for | "making something unclear" does not fit "confusing for" |
| Unit 33 | highlight | to emphasize; emphasize; underscore | to draw attention to something; emphasize; underscore | "emphasize" was listed twice |
| Unit 35 | borrows | takes and uses something temporarily; loans; takes | takes and uses something from another source, such as an idea; takes; adopts | "loans" means the opposite (lends) |
| Unit 35 | representative | typical of a group; typical; example | typical of a larger group; typical; characteristic | the synonym "example" is a noun, but the word is an adjective |
| Unit 36 | reliably | dependably; dependably; consistently | in a way that can be trusted or depended on; dependably; consistently | "dependably" was listed twice |
| Unit 38 | inconspicuousness | not easily seen; invisibility; subtlety | the quality of not being easily noticed; invisibility; subtlety | defined an adjective ("not easily seen"), but the word is a noun |
| Unit 39 | selecting | choosing; picking; choosing | carefully choosing from a group; picking; choosing | "choosing" was listed twice |
| Unit 39 | construct | to build; build; assemble | to build or put together, such as a building or an argument; assemble; form | "build" was listed twice |
| Unit 39 | foresight | ability to predict the future; anticipation; prescience | the ability to see what will be needed in the future and plan for it; anticipation; prudence | "predict the future" is misleading; "prescience" is not a plain word |
| Unit 40 | undermine | to weaken; weaken; sabotage | to gradually weaken or damage something; weaken; sabotage | "weaken" was listed twice |
| Unit 40 | understand | to comprehend; grasp; comprehend | to know the meaning of something; grasp; comprehend | "comprehend" was listed twice |
| Unit 40 | arguing about | debating; debating; disputing | disagreeing in words about something; debating; disputing | "debating" was listed twice |
| Unit 44 | enhancement | improvement; improvement; augmentation | something that makes a thing better or more valuable; improvement; upgrade | "improvement" was listed twice |
| Unit 44 | learned | acquired knowledge; educated; knowledgeable | having a lot of knowledge from long study; educated; scholarly | mixed the verb ("acquired knowledge") with adjective synonyms |
| Unit 44 | react to | to respond to; respond to; answer | to act or feel a certain way because of something; respond to; answer | "respond to" was listed twice |

Every other definition is SAT MAKON's, word for word (apart from the ligature characters mentioned in the summary).
