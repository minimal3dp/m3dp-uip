import { useConsent } from './useConsent'

interface AnalyticsEvent {
  name: string;
  params: Record<string, any>;
}

const ALLOWED_CALCULATORS = new Set([
  'rotation_distance',
  'pressure_advance',
  'orcaslicer_flow_two_pass',
  'orcaslicer_flow_yolo',
  'input_shaping'
]);

function sanitizeParams(params: Record<string, any>): Record<string, any> {
  const sanitized: Record<string, any> = {};
  for (const [k, v] of Object.entries(params)) {
    if (v === undefined || v === null) continue;
    if (typeof v === 'number' && !Number.isFinite(v)) continue;
    if (typeof v === 'string' && v.length > 200) continue; // avoid oversized payload
    sanitized[k] = v;
  }
  return sanitized;
}

let queue: AnalyticsEvent[] = [];
let flushTimer: number | undefined;
const FLUSH_INTERVAL = 4000; // 4s batching window
const MAX_QUEUE_SIZE = 10;

function sendEvent(ev: AnalyticsEvent) {
  try {
    if (typeof window !== 'undefined' && (window as any).gtag) {
      (window as any).gtag('event', ev.name, ev.params);
      if ((window as any).nuxtApp?.$config?.public?.gaDebug === 'true') {
        // eslint-disable-next-line no-console
        console.log('[GA DEBUG] sent', ev);
      }
    }
  } catch (e) {
    // silence
  }
}

function flushQueue() {
  if (!queue.length) return;
  const items = [...queue];
  queue = [];
  items.forEach(sendEvent); // GA4 gtag doesn't support true batch; simulate sequential flush
  if (flushTimer) {
    clearTimeout(flushTimer);
    flushTimer = undefined;
  }
}

function scheduleFlush() {
  if (flushTimer) return;
  flushTimer = window.setTimeout(() => flushQueue(), FLUSH_INTERVAL);
}

export const useAnalytics = () => {
  const { consent } = useConsent();

  const trackCalculatorUse = (calculator: string, data?: Record<string, any>) => {
    // Require explicit granted consent before tracking
    if (consent.value !== true) {
      if (typeof window !== 'undefined' && (window as any).nuxtApp?.$config?.public?.gaDebug === 'true') {
        // eslint-disable-next-line no-console
        console.log('[GA DEBUG] skipped (no consent)', calculator);
      }
      return;
    }
    if (!ALLOWED_CALCULATORS.has(calculator)) return;
    const params = sanitizeParams({ calculator, ...data });
    queue.push({ name: 'calculator_use', params });
    if (queue.length >= MAX_QUEUE_SIZE) {
      flushQueue();
    } else if (typeof window !== 'undefined') {
      scheduleFlush();
    }
  };

  // Immediate flush triggers (page hide/unload)
  if (typeof document !== 'undefined') {
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'hidden') flushQueue();
    });
    window.addEventListener('beforeunload', () => flushQueue());
    window.addEventListener('pagehide', () => flushQueue());
  }

  return { trackCalculatorUse, flushQueue };
};
