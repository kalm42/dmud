/* @ds-bundle: {"format":4,"namespace":"Dmud","components":[{"name":"ActionButton"},{"name":"NotebookNavigation"},{"name":"NotebookPage"},{"name":"SceneHeading"},{"name":"SceneDivider"},{"name":"StoryTurn"},{"name":"StoryEntry"},{"name":"PlayerIntention"},{"name":"KnownCharacter"},{"name":"MessageComposer"},{"name":"ResponseStatus"},{"name":"CharacterCard"},{"name":"ReferenceOverlay"},{"name":"MechanicalResult"},{"name":"JournalEntry"},{"name":"StatAssignment"},{"name":"AttributeAllocation"},{"name":"SaveSlot"},{"name":"SystemNotice"},{"name":"AwardNotice"}]} */
(function () {
  "use strict";
  var React = window.React;
  var h = React.createElement;
  var useState = React.useState, useEffect = React.useEffect, useRef = React.useRef, useId = React.useId;

  function cx() {
    var out = [];
    for (var i = 0; i < arguments.length; i++) if (arguments[i]) out.push(arguments[i]);
    return out.join(" ");
  }
  function omit(obj, keys) {
    var o = {};
    for (var k in obj) if (Object.prototype.hasOwnProperty.call(obj, k) && keys.indexOf(k) < 0) o[k] = obj[k];
    return o;
  }

  var ATTRS = ["Body", "Agility", "Constitution", "Mind", "Presence"];
  var ARRAY = [8, 10, 12, 13, 14];

  /* ActionButton ------------------------------------------------------ */
  function ActionButton(props) {
    var id = useId();
    var variant = props.variant || "primary";
    var rest = omit(props, ["variant", "disabledReason", "className", "children"]);
    var reasonId = props.disabled && props.disabledReason ? id + "-why" : undefined;
    var btn = h("button", Object.assign({ type: "button" }, rest, {
      className: cx("dm-btn", "dm-btn--" + variant, props.className),
      "aria-describedby": reasonId
    }), props.children);
    if (!reasonId) return btn;
    return h("span", { className: "dm-btn-wrap" }, btn, h("span", { id: reasonId, className: "dm-caption dm-btn-why" }, props.disabledReason));
  }

  /* NotebookNavigation ------------------------------------------------ */
  function NotebookNavigation(props) {
    var items = props.items || [];
    return h("nav", { className: cx("dm-nav", props.className), "aria-label": props.label || "Notebook" },
      props.title ? h("p", { className: "dm-nav-title" }, props.title) : null,
      h("ul", { className: "dm-nav-list" }, items.map(function (it) {
        var current = it.id === props.currentId;
        return h("li", { key: it.id },
          h("button", {
            type: "button",
            className: cx("dm-nav-item", current && "is-current"),
            "aria-current": current ? "page" : undefined,
            onClick: function () { props.onSelect && props.onSelect(it.id); }
          },
            h("span", { className: "dm-nav-marker", "aria-hidden": "true" }, current ? "▸" : ""),
            h("span", null, it.label)));
      })));
  }

  /* NotebookPage ------------------------------------------------------ */
  function NotebookPage(props) {
    var Tag = props.as || "main";
    return h(Tag, { className: cx("dm-page", props.plain && "dm-page--plain", props.className), "aria-label": props.label },
      props.plain ? null : h("span", { className: "dm-page-star dm-page-star--l", "aria-hidden": "true" }, "\u2726"),
      props.plain ? null : h("span", { className: "dm-page-star dm-page-star--r", "aria-hidden": "true" }, "\u2726"),
      props.children);
  }

  /* SceneHeading ------------------------------------------------------ */
  function SceneHeading(props) {
    var Tag = "h" + (props.level || 2);
    return h("header", { className: cx("dm-scene", props.className) },
      h(Tag, { className: "dm-scene-title" }, props.title),
      props.detail ? h("p", { className: "dm-caption dm-scene-detail" }, props.detail) : null);
  }

  /* SceneDivider ------------------------------------------------------ */
  function SceneDivider(props) {
    return h("div", { className: cx("dm-divider", props.className), "aria-hidden": "true" },
      h("svg", { viewBox: "0 0 240 24", width: 240, height: 24, focusable: "false" },
        h("path", { d: "M4 12h84M152 12h84" }),
        h("path", { d: "M88 12c10-10 22-10 32 0c10 10 22 10 32 0" }),
        h("path", { d: "M88 12c10 10 22 10 32 0c10-10 22-10 32 0" }),
        h("circle", { cx: 120, cy: 12, r: 3 }), h("circle", { cx: 4, cy: 12, r: 2 }), h("circle", { cx: 236, cy: 12, r: 2 })));
  }

  /* Transcript rows: a margin label beside the text ------------------ */
  function Row(cls, margin, main, ariaLabel) {
    return h("article", { className: cls, "aria-label": ariaLabel },
      h("div", { className: "dm-margin" }, margin),
      h("div", { className: "dm-main" }, main));
  }
  function SrOnly(text) { return h("span", { className: "dm-sr" }, text); }

  /* StoryTurn --------------------------------------------------------- */
  function StoryTurn(props) {
    return h("section", { className: cx("dm-turn", props.className), "aria-label": props.label },
      props.time ? h("div", { className: "dm-turn-time" }, h("p", { className: "dm-caption" }, props.time)) : null,
      props.children);
  }

  /* StoryEntry -------------------------------------------------------- */
  var VOICE = {
    narration: { name: "Narration" },
    rowan: { name: "Rowan", sub: "your DM" },
    clarification: { name: "Rowan", sub: "needs a detail" },
    failure: { name: "Not committed" }
  };
  function StoryEntry(props) {
    var kind = props.kind || "narration";
    var name, sub, margin;
    if (kind === "npc") { name = props.speaker || "Someone"; sub = props.epithet; }
    else { name = props.label || VOICE[kind].name; sub = VOICE[kind].sub; }
    var aria = name + (sub ? ", " + sub : "");
    if (props.continued) {
      margin = SrOnly(aria + " (continued)");
    } else if (kind === "npc" && props.onIdentify) {
      margin = h("button", { type: "button", className: "dm-speaker", "aria-haspopup": "dialog", onClick: props.onIdentify },
        h("span", { className: "dm-speaker-name" }, name),
        sub ? h("span", { className: "dm-speaker-sub" }, sub) : null,
        SrOnly(" — what you know"));
    } else {
      margin = h("p", { className: "dm-voice" },
        h("span", { className: "dm-voice-name" }, name),
        sub ? h("span", { className: "dm-voice-sub" }, sub) : null);
    }
    return Row(cx("dm-row", "dm-entry", "dm-entry--" + kind, props.continued && "is-continued", props.dropCap && "has-dropcap", props.className), margin,
      [h("div", { key: "b", className: "dm-entry-body dm-story" }, props.children),
       props.mechanic ? h("div", { key: "m", className: "dm-entry-mech" }, props.mechanic) : null], aria);
  }

  /* PlayerIntention --------------------------------------------------- */
  var INTENT_STATUS = { sent: "Sent", pending: "Rowan is working", clarification: "Rowan asked a question", resolved: "Resolved", interrupted: "Interrupted", failed: "Failed — not committed" };
  function PlayerIntention(props) {
    var status = props.status || "sent";
    var margin = h("p", { className: "dm-voice" },
      h("span", { className: "dm-voice-name" }, "You"),
      props.characterName ? h("span", { className: "dm-voice-sub" }, "as " + props.characterName) : null);
    return Row(cx("dm-row", "dm-intent-row", props.className), margin,
      h("div", { className: cx("dm-intent", "dm-intent--" + status) },
        h("p", { className: "dm-interface dm-intent-text" }, props.text),
        h("p", { className: "dm-intent-status" }, INTENT_STATUS[status] || status)),
      "You" + (props.characterName ? ", as " + props.characterName : "") + " — intention");
  }

  /* KnownCharacter ---------------------------------------------------- */
  function KnownCharacter(props) {
    var facts = props.facts || [];
    return h("div", { className: cx("dm-known", props.className) },
      props.epithet ? h("p", { className: "dm-known-epithet" }, props.epithet) : null,
      h("h3", { className: "dm-known-head" }, "What you know"),
      facts.length
        ? h("ul", { className: "dm-known-facts" }, facts.map(function (f, i) {
            return h("li", { key: i }, h("p", { className: "dm-interface" }, f.text), f.source ? h("p", { className: "dm-caption" }, f.source) : null);
          }))
        : h("p", { className: "dm-interface" }, "Nothing yet beyond what you've seen here."),
      props.lastSeen ? h("p", { className: "dm-caption dm-known-seen" }, "Last seen: " + props.lastSeen) : null,
      h("p", { className: "dm-caption dm-known-note" }, "Only what " + (props.characterName || "you") + " has seen, heard or been told. Checking this takes no time in the world."));
  }

  /* MessageComposer --------------------------------------------------- */
  function MessageComposer(props) {
    var id = useId();
    var controlled = props.value !== undefined;
    var st = useState(props.defaultValue || "");
    var value = controlled ? props.value : st[0];
    function set(v) { if (!controlled) st[1](v); props.onChange && props.onChange(v); }
    function submit() {
      if (!value.trim() || props.disabled) return;
      props.onSubmit && props.onSubmit(value);
      if (!controlled) st[1]("");
    }
    return h("form", { className: cx("dm-composer", props.className), onSubmit: function (e) { e.preventDefault(); submit(); } },
      h("label", { htmlFor: id, className: "dm-label dm-composer-label" }, props.label || "Tell Rowan what you do, say, or want to know"),
      h("div", { className: "dm-composer-row" },
        h("textarea", {
          id: id, className: "dm-composer-field", rows: props.rows || 3, value: value,
          placeholder: props.placeholder, "aria-describedby": id + "-hint",
          onChange: function (e) { set(e.target.value); },
          onKeyDown: function (e) { if (e.key === "Enter" && !e.shiftKey && !e.nativeEvent.isComposing) { e.preventDefault(); submit(); } }
        }),
        h(ActionButton, { type: "submit", disabled: props.disabled || !value.trim() }, props.submitLabel || "Send")),
      h("p", { id: id + "-hint", className: "dm-caption dm-composer-hint" }, "Enter sends · Shift+Enter adds a line"));
  }

  /* ResponseStatus ---------------------------------------------------- */
  var STATUS_TEXT = {
    pending: "Rowan is working",
    clarification: "Rowan needs one detail before anything happens",
    resolved: "Rowan has answered",
    interrupted: "Interrupted",
    failed: "Rowan couldn't answer"
  };
  function ResponseStatus(props) {
    var state = props.state || "pending";
    var main = props.message || STATUS_TEXT[state];
    return h("div", { className: cx("dm-status", "dm-status--" + state, props.className) },
      h("div", { role: "status", "aria-live": "polite", className: "dm-status-main" },
        state === "pending" ? h("span", { className: "dm-status-mark", "aria-hidden": "true" }, h("span", null), h("span", null), h("span", null)) : null,
        h("span", { className: "dm-interface-strong" }, main)),
      state === "pending" && props.quip ? h("p", { className: "dm-caption dm-status-quip", "aria-hidden": "true" }, "Backstage: " + props.quip) : null,
      props.detail ? h("p", { className: "dm-caption dm-status-detail" }, props.detail) : null,
      (state === "failed" || state === "interrupted") && props.onRetry
        ? h("div", { className: "dm-status-actions" }, h(ActionButton, { onClick: props.onRetry }, props.retryLabel || "Try again"))
        : null);
  }

  /* CharacterCard ----------------------------------------------------- */
  function CharacterCard(props) {
    var mono = props.monogram || (props.name || "?").slice(0, 1);
    return h("section", { className: cx("dm-card", props.className), "aria-label": "Your character" },
      h("p", { className: "dm-label" }, "Your character"),
      h("div", { className: "dm-card-id" },
        h("span", { className: "dm-card-mono", "aria-hidden": "true" }, mono),
        h("div", null,
          h("p", { className: "dm-card-name" }, props.name),
          props.descriptor ? h("p", { className: "dm-caption dm-card-desc" }, props.descriptor) : null)),
      props.facts && props.facts.length ? h("dl", { className: "dm-card-facts" }, props.facts.map(function (f) {
        return h("div", { key: f.label }, h("dt", null, f.label), h("dd", null, f.value));
      })) : null,
      props.onOpen ? h(ActionButton, { variant: "quiet", onClick: props.onOpen, className: "dm-card-open" }, "Open character sheet") : null);
  }

  /* ReferenceOverlay -------------------------------------------------- */
  var FOCUSABLE = 'a[href],button:not([disabled]),input:not([disabled]),select:not([disabled]),textarea:not([disabled]),[tabindex]:not([tabindex="-1"])';
  function ReferenceOverlay(props) {
    var panel = useRef(null);
    var id = useId();
    useEffect(function () {
      if (!props.open) return;
      var invoker = document.activeElement;
      var el = panel.current;
      var first = el && el.querySelector(FOCUSABLE);
      if (props.autoFocus !== false) (first || el).focus();
      function onKey(e) {
        if (e.key === "Escape") { e.stopPropagation(); props.onClose && props.onClose(); return; }
        if (e.key !== "Tab" || !el) return;
        var f = el.querySelectorAll(FOCUSABLE);
        if (!f.length) { e.preventDefault(); return; }
        var a = f[0], z = f[f.length - 1];
        if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); }
        else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); }
      }
      document.addEventListener("keydown", onKey, true);
      return function () {
        document.removeEventListener("keydown", onKey, true);
        if (invoker && invoker.focus) invoker.focus();
      };
    }, [props.open]);
    if (!props.open) return null;
    return h("div", { className: cx("dm-overlay", props.contained && "dm-overlay--contained") },
      h("div", { className: "dm-overlay-backdrop", onClick: props.onClose, "aria-hidden": "true" }),
      h("div", { ref: panel, role: "dialog", "aria-modal": "true", "aria-labelledby": id, tabIndex: -1, className: cx("dm-overlay-panel", props.className) },
        h("header", { className: "dm-overlay-head" },
          h("h2", { id: id, className: "dm-overlay-title" }, props.title),
          h("button", { type: "button", className: "dm-overlay-close", onClick: props.onClose }, "Close")),
        h("div", { className: "dm-overlay-body" }, props.children)));
  }

  /* MechanicalResult -------------------------------------------------- */
  function MechanicalResult(props) {
    var rolled = props.rolled !== false;
    return h("div", { className: cx("dm-mech", props.className) },
      h("p", { className: "dm-mech-line" },
        h("span", { className: "dm-mech-skill" }, props.skill),
        h("span", { "aria-hidden": "true" }, " · "),
        h("span", null, rolled ? (props.roll ? "rolled " + props.roll : "rolled") : "no roll needed"),
        h("span", { "aria-hidden": "true" }, " · "),
        h("span", { className: "dm-mech-result" }, props.result)),
      h("button", { type: "button", className: "dm-mech-details", "aria-haspopup": "dialog", onClick: props.onDetails },
        "Details", SrOnly(" of the " + props.skill + " " + (rolled ? "roll" : "check"))));
  }

  /* JournalEntry ------------------------------------------------------ */
  function JournalEntry(props) {
    return h("article", { className: cx("dm-journal", props.className) },
      h("div", { className: "dm-journal-head" },
        h("h3", { className: "dm-journal-title" }, props.title),
        props.status ? h("p", { className: "dm-label dm-journal-status" }, props.status) : null),
      h("div", { className: "dm-interface dm-journal-body" }, props.children),
      props.source ? h("p", { className: "dm-caption dm-journal-source" }, props.source) : null);
  }

  /* StatAssignment ---------------------------------------------------- */
  function validateArray(a) {
    var errs = [], counts = {};
    ATTRS.forEach(function (k) { var v = a[k]; if (v == null || v === "") errs.push(k + " has no value yet."); else counts[v] = (counts[v] || 0) + 1; });
    ARRAY.forEach(function (v) {
      if ((counts[v] || 0) > 1) errs.push(v + " is used " + counts[v] + " times — each value goes to exactly one attribute.");
      else if (!counts[v]) errs.push(v + " hasn't been assigned.");
    });
    return errs;
  }
  function StatAssignment(props) {
    var st = useState(props.defaultValue || {});
    var controlled = props.value !== undefined;
    var val = controlled ? props.value : st[0];
    var errors = validateArray(val);
    var locked = !!props.locked;
    var id = useId();
    function set(k, v) {
      var next = Object.assign({}, val); next[k] = v === "" ? null : Number(v);
      if (!controlled) st[1](next); props.onChange && props.onChange(next);
    }
    var used = {}; ATTRS.forEach(function (k) { if (val[k] != null) used[val[k]] = (used[val[k]] || 0) + 1; });
    return h("fieldset", { className: cx("dm-stats", locked && "is-locked", props.className), "aria-describedby": id + "-msg" },
      h("legend", { className: "dm-label" }, locked ? "Starting stats · locked" : "Assign 8, 10, 12, 13 and 14 — each once"),
      h("div", { className: "dm-stats-grid" }, ATTRS.map(function (k) {
        var v = val[k];
        var dup = v != null && used[v] > 1;
        var missing = v == null;
        return h("div", { key: k, className: cx("dm-stat", dup && "is-invalid", !dup && !missing && "is-set") },
          h("label", { htmlFor: id + k, className: "dm-interface-strong" }, k),
          locked
            ? h("p", { id: id + k, className: "dm-stat-value" }, v != null ? v : "—")
            : h("select", { id: id + k, className: "dm-stat-select", value: v == null ? "" : String(v), "aria-invalid": dup || undefined, onChange: function (e) { set(k, e.target.value); } },
              h("option", { value: "" }, "Choose"),
              ARRAY.map(function (n) { return h("option", { key: n, value: String(n) }, n + (used[n] && v !== n ? " (in use)" : "")); })),
          h("p", { className: "dm-caption dm-stat-state" }, locked ? "Locked" : dup ? "Duplicate" : missing ? "Unassigned" : "Assigned"));
      })),
      h("div", { id: id + "-msg", className: "dm-stats-msg", role: "status", "aria-live": "polite" },
        locked ? h("p", { className: "dm-caption" }, "Confirmed with Rowan. Starting stats no longer change.")
          : errors.length ? h("ul", { className: "dm-stats-errors" }, errors.map(function (e) { return h("li", { key: e }, e); }))
            : h("p", { className: "dm-stats-ok" }, "All five assigned. Ready to confirm.")),
      !locked && props.onConfirm ? h(ActionButton, { disabled: errors.length > 0, disabledReason: errors.length ? "Fix the assignments above first." : undefined, onClick: function () { props.onConfirm(val); } }, "Confirm starting stats") : null);
  }

  /* AttributeAllocation ----------------------------------------------- */
  function AttributeAllocation(props) {
    var attrs = props.attributes || {};
    var earned = props.earned || 0, spent = props.spent || 0;
    var unspent = earned - spent;
    var pv = useState(null), preview = pv[0], setPreview = pv[1];
    var state = props.state || "idle";
    var id = useId();
    var over = preview && unspent < 1;
    return h("section", { className: cx("dm-alloc", props.className), "aria-labelledby": id },
      h("h3", { id: id, className: "dm-label" }, "Attribute points"),
      h("p", { className: "dm-interface dm-alloc-counts" },
        h("span", null, "Earned ", h("b", null, earned)), " · ",
        h("span", null, "Spent ", h("b", null, spent)), " · ",
        h("span", null, "Unspent ", h("b", null, unspent))),
      h("ul", { className: "dm-alloc-list" }, ATTRS.map(function (k) {
        var sel = preview === k;
        return h("li", { key: k, className: cx("dm-alloc-row", sel && (over ? "is-invalid" : "is-preview")) },
          h("span", { className: "dm-interface-strong" }, k),
          h("span", { className: "dm-alloc-val" }, attrs[k] != null ? attrs[k] : "—", sel ? " → " + ((attrs[k] || 0) + 1) : ""),
          h("button", { type: "button", className: "dm-alloc-pick", "aria-pressed": sel, disabled: state === "pending", onClick: function () { setPreview(sel ? null : k); } }, sel ? "Previewing +1" : "Preview +1"));
      })),
      h("div", { role: "status", "aria-live": "polite", className: "dm-alloc-msg" },
        over ? h("p", { className: "dm-alloc-error" }, "No unspent points — this would overspend by 1. Nothing changed.")
          : state === "pending" ? h("p", { className: "dm-caption" }, "Saving your choice…")
            : state === "persisted" ? h("p", { className: "dm-caption" }, "Saved. The character sheet shows the new value.")
              : preview ? h("p", { className: "dm-caption" }, "Preview only — confirm to spend 1 point on " + preview + ".")
                : unspent < 1 ? h("p", { className: "dm-caption" }, "No unspent points.") : null),
      h(ActionButton, {
        disabled: !preview || over || state === "pending",
        disabledReason: !preview ? "Preview an increase first." : over ? "Not enough unspent points." : undefined,
        onClick: function () { props.onConfirm && props.onConfirm(preview); }
      }, "Confirm +1 " + (preview || "")));
  }

  /* SaveSlot ---------------------------------------------------------- */
  function SaveSlot(props) {
    var sel = !!props.selected;
    if (props.empty) {
      return h("button", { type: "button", className: cx("dm-slot", "is-empty", sel && "is-selected", props.className), "aria-pressed": sel, onClick: props.onSelect },
        h("span", { className: "dm-label" }, "Slot " + props.slot + (sel ? " · Selected" : "")),
        h("span", { className: "dm-interface" }, "Empty slot"));
    }
    return h("button", { type: "button", className: cx("dm-slot", sel && "is-selected", props.className), "aria-pressed": sel, onClick: props.onSelect },
      h("span", { className: "dm-label" }, "Slot " + props.slot + (sel ? " · Selected" : "")),
      h("span", { className: "dm-slot-campaign" }, props.campaign),
      h("span", { className: "dm-interface" }, [props.place, props.worldTime].filter(Boolean).join(" · ")),
      props.savedAt ? h("span", { className: "dm-caption dm-slot-saved" }, "Saved " + props.savedAt) : null);
  }

  /* SystemNotice (deferred P7–P8) ------------------------------------- */
  function SystemNotice(props) {
    return h("aside", { className: cx("dm-system", props.className), "aria-label": "The System" },
      h("p", { className: "dm-label dm-system-label" }, props.label || "The System"),
      h("div", { className: "dm-interface" }, props.children));
  }

  /* AwardNotice (deferred P6–P8) -------------------------------------- */
  var AWARD = { achievement: "Achievement", title: "Title", prize: "Prize", variant: "Earned variant" };
  function AwardNotice(props) {
    var t = AWARD[props.type] || "Award";
    return h("aside", { className: cx("dm-award", props.className), "aria-label": t + ": " + props.name },
      h("p", { className: "dm-label dm-award-label" }, t + " earned"),
      h("p", { className: "dm-award-name" }, props.name),
      props.children ? h("div", { className: "dm-interface" }, props.children) : null);
  }

  var api = {
    ActionButton: ActionButton, NotebookNavigation: NotebookNavigation, NotebookPage: NotebookPage, SceneHeading: SceneHeading, SceneDivider: SceneDivider, StoryTurn: StoryTurn, StoryEntry: StoryEntry, KnownCharacter: KnownCharacter,
    PlayerIntention: PlayerIntention, MessageComposer: MessageComposer, ResponseStatus: ResponseStatus,
    CharacterCard: CharacterCard, ReferenceOverlay: ReferenceOverlay, MechanicalResult: MechanicalResult,
    JournalEntry: JournalEntry, StatAssignment: StatAssignment, AttributeAllocation: AttributeAllocation,
    SaveSlot: SaveSlot, SystemNotice: SystemNotice, AwardNotice: AwardNotice
  };
  window.Dmud = Object.assign(window.Dmud || {}, api);
})();
